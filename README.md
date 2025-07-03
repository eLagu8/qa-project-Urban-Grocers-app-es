# 🧪 QA Project: Urban Grocers App (ES)

This repository contains automated tests for the backend API of the **Urban Grocers** application, created as part of the **TripleTen QA Engineer Bootcamp**.

---

## 📌 Objective

To validate the Urban Grocers API endpoints through automated tests using `pytest` and `requests`, focusing on:

- User creation
- Product kit creation
- Validation of the `"name"` field in the product kit

---

## 🛠️ Technologies

- 🐍 Python 3.11
- 🧪 pytest
- 🌐 requests
- 💻 PyCharm (IDE)
- 🧾 JSON (data exchange format)

---

## 📂 Project Structure

```
qa-project-Urban-Grocers-app-es/
├── data.py                    # Reusable data: headers, body templates
├── sender_stand_request.py   # Functions to send API requests
├── create_kit_name_kit_test.py # Tests for the 'name' field in the product kit
├── configuration.py          # Dependencies (if applicable)
└── README.md                 # Project documentation
```

---

## ✅ Test Cases Implemented

### 🟢 Positive Tests
- Create a kit with a valid name (1–511 characters)
- `"name"` as a number instead of a string
- `"name"` with special characters
- `"name"` with spaces

### 🔴 Negative Tests
- `"name"` with 0 characters
- `"name"` field missing in request body
- `"name"` as other non-string types
- `"name"` with more than 512 characters


---

## 🚀 Running Tests

From terminal:

```bash
pytest create_kit_name_kit_test.py
```

From PyCharm:

1. Right-click on the file or test function `test_...`
2. Select "Run 'pytest for test_xxx'"
3. View results in the test output panel

---

## 🔍 Tips

- If PyCharm shows a **low memory warning** ("heap size"), you can increase it by editing `pycharm64.vmoptions`.
- Use `print(response.status_code, response.text)` to debug API responses.
- Any incorrect responses (e.g., `500` instead of `400`) should be documented as bugs.

---

## 📖 Additional Notes

This project is part of the **API Testing module** in the TripleTen bootcamp.  
It focuses on developing automation skills, test design, and HTTP response analysis.

---

## 👨‍💻 Author

Eduardo Lagunas – QA Tester | TripleTen Bootcamp

---