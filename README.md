# IDnow AutoIdent - Appium Python Automation

Automated test suite for IDnow AutoIdent mobile app

## 📁 Project Structure

```
My-Work-Mobile-Tests/
├── config/
│   └── config.py              # Appium capabilities and settings
├── page_objects/
│   ├── base_page.py           # Base page with common methods
│   ├── id_entry_page.py       # Ident ID entry screen
│   └── privacy_policy_page.py # Privacy policy/terms screen
├── tests/
│   ├── conftest.py            # Pytest fixtures & driver setup
│   └── test_idnow_flow.py     # Main test case
├── reports/                   # Test screenshots
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (Ident ID, platform)
└── IDnow_AutoIdent_Test_Design.md  # Test design document
```

## 🚀 Quick Start

### 1. Prerequisites

- **Python 3.8+**
- **Node.js and npm** (for Appium)
- **Appium Server 2.x**
  ```powershell
  npm install -g appium
  appium driver install uiautomator2  # For Android
  ```
- **Android Studio** with emulator/device configured

### 2. Installation

```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure

**Edit [.env](.env) file:**
- Set your `IDENT_ID` (generate from https://go.test.idnow.de/qaautoident/userdata)

**Edit [config/config.py](config/config.py):**
- Update `appPackage` and `appActivity` for Android

**Update element locators** using Appium Inspector:
- [page_objects/id_entry_page.py](page_objects/id_entry_page.py)
- [page_objects/privacy_policy_page.py](page_objects/privacy_policy_page.py)

### 4. Run Tests

```powershell
# Start Appium server (in separate terminal)
appium

# Run tests
pytest tests/ -v -s

# Generate HTML report
pytest tests/ --html=reports/report.html --self-contained-html
```

## Key Files

- **[config/config.py](config/config.py)** - Appium capabilities for Android/iOS
- **[tests/conftest.py](tests/conftest.py)** - Pytest fixtures & driver initialization
- **[page_objects/base_page.py](page_objects/base_page.py)** - Reusable page object methods
- **[tests/test_idnow_flow.py](tests/test_idnow_flow.py)** - Test implementation

---


### Environment & Data: How would you handle testability for flows that require camera or ID documents in a real project?


1. Mock/Stub Backend Services: Configure test environment to accept pre-approved test document images
2. Bypass Modes: Use feature flags or test builds that skip camera capture for automated tests
3. Test User Pool: Maintain database of test identities with pre-uploaded documents that pass validations
4. Image Injections: Use `driver.push_file()` to inject pre-captured test images directly into app storage
5. Backend API Tests: Validate document processing, OCR, liveness detection via direct API calls
6. Upload Endpoints: Post test document images directly to verification APIs


