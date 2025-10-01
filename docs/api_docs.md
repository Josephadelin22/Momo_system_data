# MoMo SMS Transactions API Documentation

## Authentication

All endpoints require **Basic Authentication**.

- Example credentials:
    - Username: `admin`
    - Password: `password123`
- Unauthorized requests yield **401 Unauthorized**.

---

## Endpoints

### 1. List All Transactions

**Endpoint:** `GET /transactions`  
**Request Example:**
GET http://localhost:8000/transactions
Authorization: Basic



**Response Example:**
[
{
"id": "8888888",
"transaction_type": "payment",
"amount": "1234",
"sender": "George",
"receiver": "Rose",
"timestamp": "2025-10-01 21:00:00"
},
...
]



**Error Codes:**
- `401 Unauthorized`: Invalid or missing credentials

---

### 2. Get One Transaction by ID

**Endpoint:** `GET /transactions/{id}`  
**Request Example:**
GET http://localhost:8000/transactions/8888888
Authorization: Basic



**Response Example:**
{
"id": "8888888",
"transaction_type": "payment",
"amount": "1234",
"sender": "George",
"receiver": "Rose",
"timestamp": "2025-10-01 21:00:00"
}



**Error Codes:**
- `401 Unauthorized`
- `404 Not found`

---

### 3. Create a Transaction

**Endpoint:** `POST /transactions`  
**Request Example:**
POST http://localhost:8000/transactions
Authorization: Basic
Content-Type: application/json
Body:
{
"id": "9999999",
"transaction_type": "received",
"amount": "2000",
"sender": "Jane",
"receiver": "Your Account",
"timestamp": "2025-10-01 22:00:00"
}



**Response Example:**
{
"id": "9999999",
"transaction_type": "received",
"amount": "2000",
"sender": "Jane",
"receiver": "Your Account",
"timestamp": "2025-10-01 22:00:00"
}



**Error Codes:**
- `401 Unauthorized`
- `404 Invalid endpoint`

---

### 4. Update a Transaction

**Endpoint:** `PUT /transactions/{id}`  
**Request Example:**
PUT http://localhost:8000/transactions/9999999
Authorization: Basic
Content-Type: application/json
Body:
{
"amount": "2500",
"receiver": "Jane Smith"
}



**Response Example:**
{
"id": "9999999",
"transaction_type": "received",
"amount": "2500",
"sender": "Jane",
"receiver": "Jane Smith",
"timestamp": "2025-10-01 22:00:00"
}



**Error Codes:**
- `401 Unauthorized`
- `404 Not found`
- `404 Invalid endpoint`

---

### 5. Delete a Transaction

**Endpoint:** `DELETE /transactions/{id}`  
**Request Example:**
DELETE http://localhost:8000/transactions/9999999
Authorization: Basic



**Response Example:**
{
"id": "9999999",
"transaction_type": "received",
"amount": "2500",
"sender": "Jane",
"receiver": "Jane Smith",
"timestamp": "2025-10-01 22:00:00"
}



**Error Codes:**
- `401 Unauthorized`
- `404 Not found`
- `404 Invalid endpoint`
