# IDnow AutoIdent Test Design Document

**Project:** IDnow AutoIdent Mobile App 
**Test Scope:** Basic Identification Flow

---

## 1. Overview

### Test Objective
Validate that users can successfully open the app and navigate to the scan the document section after accepting the privacy policy.

---

## 2. Happy Path - Test Flow

### Test Case: TC_001_Open_App_and_Navigations

**Preconditions:**
- Valid ident ID generated from https://go.test.idnow.de/qaautoident/userdata
- IDnow AutoIdent app installed on test device (iOS/Android)
- Device has stable internet connectivity
- Device camera permissions granted

**Test Steps:**

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Launch IDnow AutoIdent app | App launches successfully, Ident-ID entry screen displayed |
| 2 | Verify ident ID input field is present | Input field visible with placeholder 'Ident-ID' |
| 3 | Enter valid ident ID | ID entered, 'Start button is active' |
| 4 | Tap Start button | Navigation to 'Terms and Conditions' screen with links |
| 5 | Verify privacy policy content displayed | Policy text visible with checkbox and links, "Start Identification" button present |
| 6 | Tap "Start Identification" button | Navigation to next steps screen with 'OK, I'm ready' button and scan your id text | 
| 7 | Tap "OK, I'm ready" button | "Scan your document" title and "OK I am ready" button visible |

---

## 3. Negative & Edge Case Scenarios

### Test Case: TC_002_Invalid_Ident_ID

**Scenario:** User enters an invalid Ident-ID

**Steps:**
1. Launch app
2. Enter invalid Ident ID
3. Tap Start

**Expected Result:**
- Start button should be active when entered the ID (When entered ID character count matches)
- Error message displayed: "Invalid Ident-ID" or error message
- User remains on ident ID entry screen for next try

---

### Test Case: TC_003_Network_Failure_During_Start

**Scenario:** Network disconnects after entering ident ID

**Steps:**
1. Launch app
2. Enter valid ident ID
3. Simulate network disconnection (Airplane mode or network conditioning)
4. Tap Start

**Expected Result:**
- "No internet connection" message
- Graceful error handling

---

## 4. Risks, Limitations & Constraints

1. Test data privacy - Use only test environment Ident IDs
2. Biometric data handling - Risk of capturing facial recognition data unintentionally; ensure tests stop before liveness detections
3. Camera hardware dependency - Automated tests cannot reliably interact with native camera APIs, requires mocking or specialized tools
3. OS versions - API behavior differences across OS versions
4. Screen size variations - Element positioning differs across devices


