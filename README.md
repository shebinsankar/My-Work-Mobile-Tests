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
# Navigate to project directory
cd d:\My-Projects\My-Work-Mobile-Tests

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Edit .env file and set your Ident ID
# (Already exists in project root)
```

### 3. Configure App Details

Edit [config/config.py](config/config.py) and update:
- `appPackage` - Your app's package name
- `appActivity` - Your app's main activity
- Device name and platform version
- Path to APK file (if using local APK)

### 4. Update Element Locators

Use **Appium Inspector** to find actual element locators:
```powershell
npm install -g appium-inspector
appium-inspector
```

Update locators in:
- [page_objects/id_entry_page.py](page_objects/id_entry_page.py)
- [page_objects/privacy_policy_page.py](page_objects/privacy_policy_page.py)

### 5. Run Tests

```powershell
# Start Appium server (in separate terminal)
appium

# Run tests
pytest tests/ -v -s

# Generate HTML report
pytest tests/ --html=reports/report.html --self-contained-html
```

## 🔧 Key Files

- **[config/config.py](config/config.py)** - Appium capabilities for Android/iOS
- **[tests/conftest.py](tests/conftest.py)** - Pytest fixtures & driver initialization
- **[page_objects/base_page.py](page_objects/base_page.py)** - Reusable page object methods
- **[tests/test_idnow_flow.py](tests/test_idnow_flow.py)** - Test implementation

