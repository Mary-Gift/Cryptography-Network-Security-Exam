# Network Traffic Filtering & Firewall Test Results

## Environment Details
* **Student Records Server IP:** `10.0.0.50`
* **Guest Subnet:** `192.168.100.0/24`
* **Staff Subnet:** `192.168.10.0/24`
* **Protected Service:** SSH (Port 22)

---

## Test Cases

### 1. Permitted Connection Test (Staff Access)
* **Objective:** Verify that an authorized staff member can connect to the records server service.
* **Test Command (Run from Staff Subnet):**
  ```bash
  ssh staff_user@10.0.0.50
  ```
* **Expected Outcome:** Connection is successful and prompts for password/key.

* **Actual Result:** Connection established successfully (Port 22 reachable).

## 2. Blocked Connection Test 1 (Guest Access to Records Server)

* **Objective:** Verify that users on the guest network cannot access the student records server.

* **Test Command (Run from Guest Subnet):**

```Bash
ping -c 3 10.0.0.50
# OR testing service port
nc -zv 10.0.0.50 22
```

* **Expected Outcome: Request timed out / Connection refused or dropped by firewall rule.**

* **Actual Result:** Packets dropped. No route/connection to the server from the guest IP range.

## 3. Blocked Connection Test 2 (Unauthorized External/Other Access to Service)

* **Objective:** Verify that unauthorized external IP addresses cannot access port 22 on the records server.

* **Test Command (Run from external/unauthorized network):**
```Bash
  nc -zv 10.0.0.50 22
```

* **Expected Outcome:** Connection timed out / Blocked by default policy or rule.

Actual Result: Connection timed out (Blocked successfully).
  
