/**
 * Hotel Saikrupa: booking and enquiry backend (Google Apps Script).
 * Runs in the sadanand.kotasthane@gmail.com account (the sheet and folder live there).
 * Two worksheets in the sheet:
 *   "Adv Booking - Paid": advance payments with the screenshot and reference code.
 *   "Enquiries": every website enquiry (availability, group, details sent on WhatsApp).
 * Enquiries are logged before the guest opens WhatsApp. WhatsApp messages sent directly
 * by customers are logged by staff in the Enquiries sheet.
 */
var SHEET_ID = 'PASTE_SHEET_ID_HERE';
var FOLDER_ID = 'PASTE_DRIVE_FOLDER_ID_HERE';
var ALERT_EMAILS = ['hotelsaikrupabooking@gmail.com', 'sadanand.kotasthane@gmail.com'];

var PAID_SHEET_NAME = 'Adv Booking - Paid';
var ENQ_SHEET_NAME = 'Enquiries';
var TIERS = {500: true, 1000: true, 1500: true};          // advance amounts in Rs
var MAX_SCREENSHOT_BYTES = 3 * 1024 * 1024;               // 3 MB
var ENQUIRY_TYPES = {availability: 'Check availability form', group: 'Group enquiry (above 4 rooms)', details: 'Details sent on WhatsApp (online booking)'};

var PAID_HEADERS = ['Received at', 'Reference code', 'Advance paid (Rs)', 'Total bill incl. GST (Rs)',
  'Name', 'City', 'Mobile', 'Check-in', 'Check-out', 'Nights', 'Adults', 'Children (above 5)',
  'Room type', 'Rooms', 'Aadhaar last 4 (optional)', 'Consent given', 'Screenshot link',
  'Receipt sent (Y/N)', 'Notes', 'Retention review date'];
var ENQ_HEADERS = ['Received at', 'Type', 'Reference', 'Name', 'Mobile', 'City', 'Check-in', 'Nights',
  'Adults', 'Children up to 5', 'Children above 5', 'Rooms / room type', 'Source', 'Status', 'Handled by', 'Notes'];

/** Entry point for the website (POST, JSON in the body). */
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    if (data.website) return reply({ ok: true });            // honeypot: a bot filled the hidden field
    var ss = SpreadsheetApp.openById(SHEET_ID);
    if (data.type && data.type !== 'advance') return handleEnquiry(ss, data);
    return handleAdvance(ss, data);
  } catch (err) {
    return reply({ ok: false, error: 'Something went wrong. Please WhatsApp us on 8262 800 200.' });
  }
}

/** Quick check in a browser: confirms the web app is running. */
function doGet() {
  return reply({ ok: true, service: 'Hotel Saikrupa booking and enquiries' });
}

// ---------- advance payments ----------

function handleAdvance(ss, data) {
  var check = validateAdvance(data);
  if (check) return reply({ ok: false, error: check });
  var sheet = getOrCreate(ss, PAID_SHEET_NAME, PAID_HEADERS);
  var code = newCode(sheet, 2, data.name, 'O-ADV', Number(data.advance));
  var link = saveScreenshot(data, code);
  var now = new Date();
  sheet.appendRow([
    stamp(now), code, data.advance, data.total || '',
    data.name, data.city || '', data.mobile, data.checkin, data.checkout, data.nights,
    data.adults, data.children || 0, data.roomType || '', data.rooms || 1,
    data.aadhaar4 || '', data.consent ? 'Yes' : 'No', link, 'N', '',
    stamp(addYears(now, 3)).split(' ')[0]
  ]);
  sendAlert(code, data, link);
  return reply({ ok: true, code: code });
}

function validateAdvance(d) {
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

// ---------- enquiries (every type) ----------

function handleEnquiry(ss, d) {
  if (!ENQUIRY_TYPES[d.type]) return reply({ ok: false, error: 'Unknown enquiry type.' });
  if (d.mobile && !/^[0-9]{10}$/.test(String(d.mobile).replace(/\s+/g, ''))) {
    return reply({ ok: false, error: 'Please enter a 10-digit mobile number.' });
  }
  var sheet = getOrCreate(ss, ENQ_SHEET_NAME, ENQ_HEADERS);
  var prefix = d.type === 'group' ? 'GRP' : 'ENQ';
  // The website makes the reference (so the WhatsApp message and the sheet match). Use it if it is well formed.
  var code = /^(GRP|ENQ)-[0-9]{6}-[0-9]{4}$/.test(String(d.ref || '')) ? String(d.ref) : newCode(sheet, 3, d.name || 'GUEST', prefix, '');
  var now = new Date();
  sheet.appendRow([
    stamp(now), ENQUIRY_TYPES[d.type], code,
    d.name || '', d.mobile || '', d.city || '', d.checkin || '', d.nights || '',
    d.adults || '', d.small || 0, d.big || 0, d.rooms || '',
    d.source || '', 'New', '', ''
  ]);
  if (d.type === 'group') sendGroupAlert(code, d);
  return reply({ ok: true, code: code });
}

function sendGroupAlert(code, d) {
  MailApp.sendEmail({
    to: ALERT_EMAILS.join(','),
    subject: 'Group enquiry ' + code + ' (more than 4 rooms)',
    body: 'Group enquiry logged in the Enquiries sheet.\n\nReference: ' + code + '\nName: ' + (d.name || '-') +
      '\nMobile: ' + (d.mobile || '-') + '\nCheck-in: ' + (d.checkin || '-') + '  Nights: ' + (d.nights || '-') +
      '\nAdults: ' + (d.adults || '-') + '  Children up to 5: ' + (d.small || 0) + '  Children above 5: ' + (d.big || 0) +
      '\n\nThe guest is also sending this to WhatsApp 8262 800 200 with the same reference.'
  });
}

// ---------- helpers ----------

/** Get a worksheet by name, or create it with its headers. */
function getOrCreate(ss, name, headers) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

/** Make a code like O-ADV-DDMMYY-NAME5-500-1234 or ENQ-DDMMYY-XXXX, unique in the sheet. */
function newCode(sheet, codeCol, name, prefix, amount) {
  var today = Utilities.formatDate(new Date(), 'Asia/Kolkata', 'ddMMyy');
  var letters = String(name).replace(/\s+/g, '').replace(/[^A-Za-z]/g, '').toUpperCase().substring(0, 5);
  var existing = {};
  var last = sheet.getLastRow();
  if (last > 1) {
    sheet.getRange(2, codeCol, last - 1, 1).getValues().forEach(function (r) { existing[r[0]] = true; });
  }
  for (var i = 0; i < 50; i++) {
    var digits = ('000' + Math.floor(Math.random() * 10000)).slice(-4);
    var code = prefix === 'O-ADV'
      ? 'O-ADV-' + today + '-' + letters + '-' + amount + '-' + digits
      : prefix + '-' + today + '-' + digits;
    if (!existing[code]) return code;
  }
  throw new Error('Could not create a unique code');
}

function saveScreenshot(d, code) {
  var folder = DriveApp.getFolderById(FOLDER_ID);
  var bytes = Utilities.base64Decode(d.screenshot);
  var blob = Utilities.newBlob(bytes, d.screenshotType, code + (d.screenshotType === 'image/png' ? '.png' : '.jpg'));
  return folder.createFile(blob).getUrl();
}

function sendAlert(code, d, link) {
  var body = [
    'New advance booking (manual receipt pending)', '',
    'Reference: ' + code,
    'Advance paid: Rs ' + d.advance + (d.total ? '   Total bill incl. GST: Rs ' + d.total : ''),
    'Name: ' + d.name + (d.city ? '   City: ' + d.city : ''),
    'Mobile: ' + d.mobile,
    'Check-in: ' + d.checkin + '   Check-out: ' + (d.checkout || '-') + '   Nights: ' + (d.nights || '-'),
    'Adults: ' + d.adults + '   Children above 5: ' + (d.children || 0),
    'Room type: ' + (d.roomType || '-') + '   Rooms: ' + (d.rooms || 1), '',
    'Screenshot: ' + link, '',
    'Next: confirm the payment, send the official advance receipt by hand, and reply to the guest on WhatsApp.'
  ].join('\n');
  MailApp.sendEmail({ to: ALERT_EMAILS.join(','), subject: 'Advance booking ' + code + ' (Rs ' + d.advance + ')', body: body });
}

function stamp(date) {
  return Utilities.formatDate(date, 'Asia/Kolkata', 'dd-MM-yyyy HH:mm');
}

function addYears(date, years) {
  var d = new Date(date.getTime());
  d.setFullYear(d.getFullYear() + years);
  return d;
}

function reply(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
