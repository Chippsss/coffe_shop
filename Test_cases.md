| Test Case ID | Description           | Steps                                                                 | Expected Result                                        |
| ------------ | --------------------- | --------------------------------------------------------------------- | ------------------------------------------------------ |
| CUST-01      | Customer Registration | 1. Go to `/register/` <br> 2. Enter username, password <br> 3. Submit | Account created, redirected to login                   |
| CUST-02      | Customer Login        | 1. Go to `/login/` <br> 2. Enter valid credentials                    | Redirected to `/menu/`                                 |
| CUST-03      | View Menu             | 1. Login as customer <br> 2. Visit `/menu/`                           | Menu items displayed with images, descriptions, prices |
| CUST-04      | Place Order           | 1. Select items <br> 2. Submit order                                  | Order created with `status = pending`                  |
| CUST-05      | View Cart             | 1. After placing order, redirected to cart <br> 2. Verify items       | Cart shows correct items & total                       |


| Test Case ID | Input                     | Expected Output      | Path / Condition Tested    | Remarks           |
| ------------ | ------------------------- | -------------------- | -------------------------- | ----------------- |
| WB\_MENU\_01 | Request all menu items    | List of items        | Normal execution path      | Display all items |
| WB\_MENU\_02 | Request category "coffee" | List of coffee items | Branch: category filter    | Filters menu      |
| WB\_MENU\_03 | Request invalid category  | Empty list           | Branch: category not found | Error handling    |
