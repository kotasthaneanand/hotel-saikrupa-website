/**
 * Hotel Saikrupa: advance booking backend (Google Apps Script).
 * Runs in the hotelsaikrupabooking@gmail.com account.
 * Receives an advance booking from the website, writes one row to the sheet,
 * saves the payment screenshot to Drive and emails the team.
 *
 * Set these three values once (see SETUP.md). They are not secrets, but keep them private.
 */
var SHEET_ID = 'PASTE_SHEET_ID_HERE';
var FOLDER_ID = 'PASTE_DRIVE_FOLDER_ID_HERE';
var ALERT_EMAILS = ['hotelsaikrupabooking@gmail.com', 'sadanand.kotasthane@gmail.com'];

var TIERS = {500: true, 1000: true, 1500: true};          // advance amounts in Rs
var MAX_SCREENSHOT_BYTES = 3 * 1024 * 1024;               // 3 MB
var HEADERS = ['Received at', 'Reference code', 'Advance paid (Rs)', 'Total bill incl. GST (Rs)',
  'Name', 'City', 'Mobile', 'Check-in', 'Check-out', 'Nights', 'Adults', 'Children (above 5)',
  'Room type', 'Rooms', 'Aadhaar last 4 (optional)', 'Consent given', 'Screenshot link',
  'Receipt sent (Y/N)', 'Notes', 'Retention review date'];

/** Entry point for the website form (POST, JSON in the body). */
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    if (data.website) return reply({ ok: true });          // honeypot: a bot filled the hidden field
    var check = validate(data);
    if (check) return reply({ ok: false, error: check });

    var sheet = SpreadsheetApp.openById(SHEET_ID).getSheets()[0];
    ensureHeaders(sheet);
    var code = newReferenceCode(sheet, data);
    var link = saveScreenshot(data, code);
    var now = new Date();
    var retention = addYears(now, 3);

    sheet.appendRow([
      Utilities.formatDate(now, 'Asia/Kolkata', 'dd-MM-yyyy HH:mm'), code, data.advance, data.total || '',
      data.name, data.city || '', data.mobile, data.checkin, data.checkout, data.nights,
      data.adults, data.children || 0, data.roomType || '', data.rooms || 1,
      data.aadhaar4 || '', data.consent ? 'Yes' : 'No', link, 'N', '',
      Utilities.formatDate(retention, 'Asia/Kolkata', 'dd-MM-yyyy')
    ]);

    sendAlert(code, data, link);
    return reply({ ok: true, code: code });
  } catch (err) {
    return reply({ ok: false, error: 'Something went wrong. Please WhatsApp us on 8262 800 200.' });
  }
}

/** Quick check in a browser: confirms the web app is running. */
function doGet() {
  return reply({ ok: true, service: 'Hotel Saikrupa advance booking' });
}

function validate(d) {
  if (!d.name || String(d.name).trim().length < 2) return 'Please enter your name.';
  if (!/^[0-9]{10}$/.test(String(d.mobile || '').replace(/\s+/g, ''))) return 'Please enter a 10-digit mobile number.';
  if (!d.checkin) return 'Please choose a check-in date.';
  if (!TIERS[Number(d.advance)]) return 'Advance amount is not valid.';
  if (!d.screenshot || !d.screenshotType) return 'Please upload the payment screenshot.';
  if (!/^image\/(jpeg|png)$/.test(d.screenshotType)) return 'Please upload a JPG or PNG screenshot.';
  if (Math.ceil(String(d.screenshot).length * 3 / 4) > MAX_SCREENSHOT_BYTES) return 'Screenshot is too large (max 3 MB).';
  if (d.aadhaar4 && !/^[0-9]{4}$/.test(d.aadhaar4)) return 'Aadhaar: enter the last 4 digits only, or leave blank.';
  return '';
}

/**
 * Reference code: O-ADV-DDMMYY-NAME5-AMOUNT-XXXX
 * DDMMYY = date of payment (today), NAME5 = first 5 letters of the name with spaces removed
 * (fewer if the name is shorter), AMOUNT = 500, 1000 or 1500, XXXX = 4 random digits, checked for duplicates.
 */
function newReferenceCode(sheet, d) {
  var today = Utilities.formatDate(new Date(), 'Asia/Kolkata', 'ddMMyy');
  var letters = String(d.name).replace(/\s+/g, '').replace(/[^A-Za-z]/g, '').toUpperCase().substring(0, 5);
  var existing = {};
  var last = sheet.getLastRow();
  if (last > 1) {
    sheet.getRange(2, 2, last - 1, 1).getValues().forEach(function (r) { existing[r[0]] = true; });
  }
  for (var i = 0; i < 50; i++) {
    var digits = ('000' + Math.floor(Math.random() * 10000)).slice(-4);
    var code = 'O-ADV-' + today + '-' + letters + '-' + Number(d.advance) + '-' + digits;
    if (!existing[code]) return code;
  }
  throw new Error('Could not create a unique code');
}

function saveScreenshot(d, code) {
  var folder = DriveApp.getFolderById(FOLDER_ID);
  var bytes = Utilities.base64Decode(d.screenshot);
  var blob = Utilities.newBlob(bytes, d.screenshotType, code + (d.screenshotType === 'image/png' ? '.png' : '.jpg'));
  var file = folder.createFile(blob);
  return file.getUrl();
}

function sendAlert(code, d, link) {
  var body = [
    'New advance booking (manual receipt pending)',
    '',
    'Reference: ' + code,
    'Advance paid: Rs ' + d.advance + (d.total ? '   Total bill incl. GST: Rs ' + d.total : ''),
    'Name: ' + d.name + (d.city ? '   City: ' + d.city : ''),
    'Mobile: ' + d.mobile,
    'Check-in: ' + d.checkin + '   Check-out: ' + (d.checkout || '-') + '   Nights: ' + (d.nights || '-'),
    'Adults: ' + d.adults + '   Children above 5: ' + (d.children || 0),
    'Room type: ' + (d.roomType || '-') + '   Rooms: ' + (d.rooms || 1),
    '',
    'Screenshot: ' + link,
    '',
    'Next: confirm the payment, send the official advance receipt by hand, and reply to the guest on WhatsApp.'
  ].join('\n');
  MailApp.sendEmail({
    to: ALERT_EMAILS.join(','),
    subject: 'Advance booking ' + code + ' (Rs ' + d.advance + ')',
    body: body
  });
}

function ensureHeaders(sheet) {
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);
  }
}

function addYears(date, years) {
  var d = new Date(date.getTime());
  d.setFullYear(d.getFullYear() + years);
  return d;
}

function reply(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
