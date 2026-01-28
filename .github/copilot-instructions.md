# QR Code Python - AI Agent Instructions

## Project Overview
A PyQt5-based GUI desktop application that generates QR codes and shortens URLs. The app converts full URLs into shortened versions and can generate corresponding QR codes for them.

## Architecture

### Component Structure
- **GUI Layer**: [interface.ui](../interface.ui) - Qt Designer XML file defining the UI structure (textboxes, buttons, labels)
- **Application Entry**: [run.py](../run.py) - Main application class `QrCodeBuilder` that loads the UI and handles events
- **Key Dependencies**:
  - `PyQt5` (5.15.11) - GUI framework with Qt Designer integration via `loadUi()`
  - `pyshorteners` (1.0.1) - URL shortening (currently using TinyURL service)
  - `qrcode` - QR code generation (imported but not yet fully implemented)

### Data Flow
1. User enters URL in `txtUrl` text field
2. Click "btnGerar" button → `on_btnGerar_clicked()` slot triggered
3. URL passed to `CREATE_SHORT_URL()` which uses TinyURL shortener
4. Shortened URL displayed in `txtUrlShort` field
5. QR code generation (partial implementation in `CREATE_QRCODE()`)

## Key Patterns & Conventions

### PyQt5 Signal-Slot Pattern
- Use `@pyqtSlot()` decorator for event handlers following naming convention: `on_<widget_name>_<signal>()`
- Example: Button click on `btnGerar` → `on_btnGerar_clicked()`
- Load UI with `loadUi("interface.ui", self)` in `__init__()` to bind widget names automatically

### UI Element Access
- Access UI elements by their Qt Designer names directly (e.g., `self.txtUrl`, `self.txtUrlShort`)
- Names defined in interface.ui and automatically injected by `loadUi()`

### Error Handling Pattern
- Display user-facing messages via `showMessage(title, message)` using `QMessageBox.information()`
- Validate input before processing (check for empty URL before shortening)

## Development Workflow

### Running the Application
```powershell
# Activate virtual environment (Windows)
.\env\Scripts\Activate.ps1

# Run the application
python run.py
```

### Project Dependencies
- All dependencies listed in [requirements.txt](../requirements.txt)
- Virtual environment in `env/` folder
- Install new packages: `pip install <package> && pip freeze > requirements.txt`

### UI Modifications
- Edit [interface.ui](../interface.ui) with Qt Designer (usually via PyQt5 tools)
- Widget names in the UI automatically become accessible as `self.<widget_name>` after `loadUi()` call
- No code generation needed - PyQt5 handles dynamic binding

## Important Integration Points

### URL Shortening Service
- Current implementation uses `Shortener().tinyurl.short(url)` from pyshorteners
- Internet-dependent operation - requires active connection
- Currently no error handling for network failures

### QR Code Generation
- `qrcode` library is imported but `CREATE_QRCODE()` function is incomplete (hardcoded "teste" value)
- Needs integration with shortened URL output and UI display widget

### Incomplete Features to Complete
1. Full QR code generation from shortened URL
2. Save QR code as image file
3. Network error handling in URL shortening
4. Input validation (URL format validation)

## Portuguese UI Text Convention
- UI labels and messages use Portuguese (e.g., "QRCODE-BUILDER" title, "Voce esquece de alguma coisa?" message)
- Follow this convention for any new user-facing messages

## Code Quality Notes
- Unused imports: `loguru`, `notify_py`, `colorama` in requirements.txt but not used in current code
- Consider removing or implementing logging/notifications if planned
