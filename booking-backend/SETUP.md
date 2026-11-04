# Advance booking backend: setup (Option A)

Account: hotelsaikrupabooking@gmail.com. Do these steps while signed in to that account.

1. **Sheet.** Google Drive → New → Google Sheets. Name it "Hotel Saikrupa Advance Bookings". Copy the sheet ID from the address bar (the long text between /d/ and /edit) and send it to Claude.
2. **Folder.** Drive → New → Folder → "Advance payment screenshots". Open it and copy the folder ID from the address bar (the text after /folders/) and send it to Claude.
3. **Script.** In the sheet, open Extensions → Apps Script. Delete the default code and paste the contents of `booking-backend/Code.gs`. Replace `PASTE_SHEET_ID_HERE` and `PASTE_DRIVE_FOLDER_ID_HERE` with the two IDs. Save (Ctrl+S).
4. **Deploy.** Click Deploy → New deployment → Select type: Web app. Execute as: Me. Who has access: Anyone. Click Deploy, approve the permissions (Sheets, Drive, Gmail), then copy the Web app URL and send it to Claude. Treat the URL as private: anyone who has it can send entries to the sheet.
5. **Test.** Open the Web app URL in a browser. It should show `{"ok":true,...}`.

Notes:
- The reference code format is O-ADV-DDMMYY-NAME5-AMOUNT-XXXX (for example O-ADV-291029-RAMLA-500-4821).
- Every entry sends an alert email to both addresses in `ALERT_EMAILS`.
- The Aadhaar field keeps the last 4 digits only, and the retention review date is set 3 years ahead.
- Nothing is public until the website form is approved and merged.
