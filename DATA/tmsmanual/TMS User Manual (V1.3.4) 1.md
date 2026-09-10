[[IMAGE: manual_img_001.png]] [[IMAGE: manual_img_002.jpg]] [[IMAGE: manual_img_003.jpg]] [[IMAGE: manual_img_004.png]]

# Introduction

About this document

The document outlines all the features included in the Koili TMS portal and provides step-by- step instructions for end users on how to use them. Screenshots are included with markers for clarity. This guide is aimed at helping role users to use the system as efficiently as possible. About koili

[[IMAGE: manual_img_005.png]] [[IMAGE: manual_img_006.jpg]]

The Terminal Management System (TMS) is an important part of the Koili ecosystem. It is a centralized portal designed to help banks manage their IPN devices and merchants easily. With TMS, users can handle tasks like creating branches, assigning user roles, and managing merchant accounts. It provides all the tools needed to simplify operations and improve how the IPN system works.

Generic information about the Terminal Management System (TMS)

- The system cannot be accessed without logging in. The system administrator will provide login details (Username). A link will be shared with the user through email to set their password by themselves.

- The Koili TMS is a web-based application. Hence, a stable internet connection is crucial. It is recommended to ensure good connectivity throughout.

- In case of unintended errors, immediate first-level support will be provided by the bank's system administrator.

- The Koili TMS platform has a separate URL for Partner users of the banks. Thus, Partner users need to log in to the system using the Partner URL.

# 1. TMS Login Process For all User Roles

Users can safely access their accounts by logging in with their username and password. They can also ensure their account's security by securely logging out after use.

- Visit the provided custom URL to log in.

- There are 7 types of user roles in the system:

System admin, Checker, Auditor, Operator, Branch operator, IT operator, and Partner.

- Username and Password are required to login to the system.

- The system admin will provide the username, whereas the user can set the password.

- An email will be sent to the user once their profile is created with a link to set the password.

- Input Username and Password. Then, click on the Sign In button as shown below.

[[IMAGE: manual_img_007.jpg]]

# 2. Dashboard

- After logging in successfully, users are directed to their Dashboard.

- The Dashboard has a side navigation bar with different sections.

- Key widgets on the Dashboard show important details like the total number of users, merchants, notifications, notification history, and allocated/unallocated IPNs, giving a clear overview of the IPN system's status.

- A "Quick Links" section provides easy access to features like Quick IPN Assign, Sync IPN, and Operations.

- The Dashboard and side navigation options are tailored to each user's role, ensuring they see only the features relevant to them.

- Below is an example of how the dashboard appears for a System Admin user:

[[IMAGE: manual_img_008.jpg]]

- Below is an example of how the dashboard appears for a Checker user:

[[IMAGE: manual_img_009.jpg]]

- Below is an example of how the dashboard appears for an Auditor user:

[[IMAGE: manual_img_010.jpg]]

- Below is an example of how the dashboard appears for an Operator user:

[[IMAGE: manual_img_011.jpg]]

- Below is an example of how the dashboard appears for a Branch Operator user:

[[IMAGE: manual_img_012.jpg]]

- Below is an example of how the dashboard appears for an IT operator user:

[[IMAGE: manual_img_013.jpg]]

- Below is an example of how the dashboard appears for an Partner user:

[[IMAGE: manual_img_014.jpg]]

## 2.1. Key Widgets

Since the auditor, checker, and system administrator have access to the dashboard, they can perform specific actions and view certain information.

- Total Users: This widget displays the total number of users of the TMS portal.

[[IMAGE: manual_img_015.jpg]]

- Total Merchants: This widget displays the total number of Merchants that have been onboarded in the client’s system.

[[IMAGE: manual_img_016.jpg]]

- Total IPNs and Operation Count: The total number of IPNs in the system is recorded in the Total IPNs widget. The total count of operation requests for Merchant and IPN in the system is denoted in the dashboard as well and the count changes in real-time as more operation requests are created.

[[IMAGE: manual_img_017.jpg]]

- Allocated/Unallocated IPNs: The total number of IPNs synced in the TMS portal is displayed in this widget. The percentage of IPNs allocated to Merchants and the number of free IPNs are also segregated. This information is also displayed in numerical form.

[[IMAGE: manual_img_018.jpg]]

# 3. Quick Links

• The Dashboard's Quick Links section offers shortcuts like Quick IPN Assign, Sync IPN, and Operations for faster access to key tasks. Check the picture to find it easily.

[[IMAGE: manual_img_019.jpg]]

## 3.1. Quick Links –Quick IPN Assign

- Hover the mouse on the Quick Links icon in the bottom-right corner of the user’s dashboard.

- Click on the Quick IPN Assign icon.

[[IMAGE: manual_img_020.jpg]]

- A Quick IPN assign dialog box appears as shown.

- Choose the Merchant or Branch option to assign an IPN to by clicking on the radio button or by searching for the respective Merchant or Branch in the search bar and clicking the checkbox to select them.

- Here, Merchant is chosen. The process is same for Branch.

[[IMAGE: manual_img_021.jpg]]

[[IMAGE: manual_img_022.jpg]]

- Click on Next.

To select an IPN, there are 2 methods: Text or Barcode.

- Choose Text or Barcode option by clicking on the radio button as shown below.

[[IMAGE: manual_img_023.jpg]]

- You can also set the number of IPNs to be visible on the page by selecting the number on the drop-down menu.

[[IMAGE: manual_img_024.jpg]]

- You can skip to next page by clicking the arrow button.

[[IMAGE: manual_img_025.jpg]].

- If you need a specific device that is not visible in the available devices list:

  - Use the search bar to look for the required IPN by entering its serial number.

  - Once found, click on the checkbox next to the IPN to select it.

- Or else

  - Select one or more devices from the available devices list by clicking their checkboxes. o After selecting the IPN(s), click the Scheme button to set the scheme identifier values for the chosen devices.

[[IMAGE: manual_img_026.jpg]]

- A scheme dialog box appears. Set the scheme identifier values and click on update.

[[IMAGE: manual_img_027.jpg]]

- The user is notified about the successful entry of scheme identifiers for the IPN selected through a status message.

Now, Enter the scheme identifiers for all the selected IPNs, respectively.

- Click on Next.

- Click on the Assign button in the Quick IPN Assign dialog box.

[[IMAGE: manual_img_028.jpg]]

- If the auto- approval is off, an IPN assign request is sent for approval and the user is notified about it with a status message.

[[IMAGE: manual_img_029.jpg]]

- The request sent needs to be verified and approved by: CHECKER or SYSTEM ADMIN USER

- For checkers, Navigate to the Approval section in the checker’s dashboard by logging to the portal.

[[IMAGE: manual_img_030.jpg]]

- Click on the checkbox of the request that needs to be approved from the Approval list.

- Click on the ellipsis icon on the Actions tab to expand a drop-down menu that contains actions such as View

Details, Approve, and Deny.

[[IMAGE: manual_img_031.jpg]]

- Click on the View Details option of the selected request to verify the details before approval.

[[IMAGE: manual_img_032.jpg]]

- A dialog box pops up with request details.

- Click on the expand button to view the detailed changed view of the request. The detailed view contains the

information of the Merchant the IPN is being assigned to and the device scheme identifiers.

[[IMAGE: manual_img_033.jpg]]

- Close the dialog box and click on the Approve option from the Actions tab for the request.

[[IMAGE: manual_img_034.jpg]]

- An approve request dialog box pops up.

- Click on the Approve button. Verify remarks aren’t mandatory.

[[IMAGE: manual_img_035.jpg]]

- The request is successfully approved, and the user is notified about it through a status message.

[[IMAGE: manual_img_036.jpg]]

- The change is reflected in the Merchant list.

- The user can check this by clicking on the Assigned IPNs option from the Actions tab for the respective Merchant.

[[IMAGE: manual_img_037.jpg]]

[[IMAGE: manual_img_038.jpg]]

- You can also set the number of merchants to be visible on the page by selecting the number on the drop-down menu.

[[IMAGE: manual_img_039.jpg]]

## 3.2. Quick links- Operation

- Hover the mouse on the Quick Links icon in the bottom-right corner of the user’s dashboard .

- Click on the Operation icon.

[[IMAGE: manual_img_040.jpg]]

- A dialog box of Operation appears. A user can view all the requests made by the user here.

[[IMAGE: manual_img_041.jpg]]

- Click the dropdown button in the Entity type tab and the Status tab and select an option to view the requests according to entity type and status type.

[[IMAGE: manual_img_042.jpg]]

[[IMAGE: manual_img_043.jpg]]

● For checker users, the operation feature is known as “Approvals” as shown.

[[IMAGE: manual_img_044.jpg]]

- Before approving any pending request, a checker can click on the View Details option by expanding the Actions tab to view the request details.

[[IMAGE: manual_img_045.jpg]]

- Click on the downward arrow to view the detailed changed view of the request.

[[IMAGE: manual_img_046.jpg]]

[[IMAGE: manual_img_047.jpg]]

Approve/ deny request

- Click on the checkbox for a specific request and click on the Approve option for that request to

approve it.

[[IMAGE: manual_img_048.jpg]]

- An Approve request dialog box pops up. Input some verified remarks (not mandatory) and click on the Approve button.

[[IMAGE: manual_img_049.jpg]]

- The request is successfully approved, and the user is notified about this through a status message.

[[IMAGE: manual_img_050.jpg]]

- The change is reflected in the system, respectively.

### 3.2.1. My Approvals

• A checker user can also view the pending requests assigned to them by clicking on the My Approval toggle as shown.

The My approvals requests are the requests assigned to the specific checker user by an operator user.

[[IMAGE: manual_img_051.jpg]]

### 3.2.2. Bulk verify

- A checker user can also approve requests in bulk by checking the box for all requests.

- Then, click on the Bulk Verify button.

[[IMAGE: manual_img_052.jpg]]

[[IMAGE: manual_img_053.jpg]]

[[IMAGE: manual_img_054.jpg]]

- A bulk verify dialog box pops up.

- Click on the Approve button. The requests are successfully approved, and the user is notified with a status message. The change is also reflected in the system accordingly.

[[IMAGE: manual_img_055.jpg]]

User can also cancel the bull approval process by clicking on the deny button.

[[IMAGE: manual_img_056.jpg]]

- The user can view the details of the approved and denied requests as well by selecting options from the drop-down menu in the status button.

[[IMAGE: manual_img_057.jpg]]

[[IMAGE: manual_img_058.jpg]]

## 3.3. Quick links- Sync IPN

Users can also sync IPNs to update if any new IPNs are added from the core system.

- To sync the IPNs, click on the sync IPN icon from the quick links.

[[IMAGE: manual_img_059.jpg]]

The system will automatically check for updates.

- If any new IPNs are added, they will be updated in the system. Otherwise, a message will be displayed stating

that everything is already up to date.

[[IMAGE: manual_img_060.jpg]]

# 4. Profile icon

- Click on profile icon in the top-right corner of the dashboard.

[[IMAGE: manual_img_061.jpg]]

- Here, you can see Profile and Logout

- Click on the Profile option to navigate to the User’s Profile section. A detailed description of the Profile section is given in the Profile section.

[[IMAGE: manual_img_062.jpg]]

- Click on the Logout option to Log out of the system.

[[IMAGE: manual_img_063.jpg]]

- A Confirm Logout dialog box pops up.

[[IMAGE: manual_img_064.jpg]]

- Click on the Logout button to log out or click on the Cancel button to cancel the Logout.

[[IMAGE: manual_img_065.jpg]]

# 5. Operation/ approval

The "Operation" segment empowers users to track and analyze operations related to Merchants and IPNs performed through the Koili TMS. It also gives access to the checker user and the system admin to review, approve, and deny requests allowing them directly to approve or deny pending requests, aligning actions with their specific roles and access permissions. The “Operation” section is displayed as the “Approvals” section in the checker user’s dashboard.

- The operation section within the operator's dashboard appears as follows:

[[IMAGE: manual_img_066.jpg]]

- You can also change the number of approved/pending/ denied to appear in a page by changing the row per page.

[[IMAGE: manual_img_067.jpg]]

- The Approvals section within the checker's dashboard appears as follows:

[[IMAGE: manual_img_068.jpg]]

- The operation/approval requests can be filtered by choosing filters according to Entity type(All, Merchant, IPN) and status type(Pending, approved, denied).

- A checker user can also view the pending requests assigned to them by clicking on the My Approval toggle as shown.

- The My approvals requests are the requests assigned to the specific checker user by an operator user.

[[IMAGE: manual_img_069.jpg]]

## 5.2. View request details (Checker dashboard)

Click on “View Details” icon before approving any pending request by expanding the Actions.

[[IMAGE: manual_img_070.jpg]]

[[IMAGE: manual_img_071.jpg]]

• Click on the downward arrow to view the detailed changed view of the request.

[[IMAGE: manual_img_072.jpg]]

## 5.3. Approve/Deny requests (Checker dashboard)

- Click on the checkbox for a specific request to approve/deny it.

- Click on the ellipses button to expand the drop-down menu.

- Then click on the Approve (✔) or Deny (✖) icon to approve or deny the request.

.[[IMAGE: manual_img_073.jpg]]

- An Approve/Deny Request dialog box pops up.

- Click on Approve or Deny button to approve or deny the request. Verify remarks are not mandatory.

[[IMAGE: manual_img_074.jpg]] [[IMAGE: manual_img_075.jpg]]

• The change is reflected in the system after approval or denial of the request respectively. The user is also notified about this through a status message.

[[IMAGE: manual_img_076.jpg]]

## 5.4. Bulk verify (Checker dashboard)

- A checker user can also approve requests in bulk by checking the box for all requests.

- Then, click on the Bulk Verify button.

[[IMAGE: manual_img_077.jpg]]

- A bulk verify dialog box pops up.

- Click on the Approve button. The requests are successfully approved and the user is notified with a status message. The change is also reflected in the system accordingly.

[[IMAGE: manual_img_078.jpg]]

- The user can view the details of the approved and denied requests as well by selecting those options from the drop-down menu in the status button according to each entity type (All, Merchant, IPN).

[[IMAGE: manual_img_079.jpg]]

# 6. Branch

Banks can create, modify, and delete branches as needed, tailoring the system to match their operational hierarchy. This feature ensures that the Koili TMS is aligned with the real branches of the bank. Through the CRUD operations (Create, Read, Update, Delete), clients can dynamically adapt their organizational layout within the system.

- Navigate to the Branch page by clicking on the Branch option from the side navigation bar.

[[IMAGE: manual_img_080.jpg]]

- You can also set the number of branches to be visible on the page by selecting the number on the drop-down menu.

[[IMAGE: manual_img_081.jpg]]

- You can skip to next page by clicking the arrow button.

[[IMAGE: manual_img_082.jpg]]

## 6.1. Import bank list from Excel

Users can now import branch details into the TMS by uploading an Excel file.

- Click on the Import Excel button.

[[IMAGE: manual_img_083.jpg]]

- Select an Excel file with bank list to import.

[[IMAGE: manual_img_084.jpg]]

- Click on Import button.

[[IMAGE: manual_img_085.jpg]]

## 6.2. Add Branch

- Click on the Add Branch button to add a new Branch.

[[IMAGE: manual_img_086.jpg]]

- Enter the details of the branch as needed.

- Click on Add.

[[IMAGE: manual_img_087.jpg]]

- The change is reflected in the system and the user is notified with a status message.

[[IMAGE: manual_img_088.jpg]]

## 6.3. View Branch Details

To view branch-specific details:

1. Open the Actions tab for a branch.

1. Click on View Details.

In this section, users can access detailed information and manage user, IPN, and merchant assignments within a branch.

[[IMAGE: manual_img_089.jpg]]

### 6.3.1. Branch User List-View Details

This section provides a categorized list of Users, IPNs, and Merchants associated with the branch. Users can toggle between each category for relevant details and actions:

[[IMAGE: manual_img_090.jpg]] a) User

In the user section, we can access, and review user details associated with the branch. We can also assign and de-assign user from the branch.

*A user can also assign users to specific branches. The default branch users are known as branch operators.

Steps to assign user to the branch:

- Click the Assign user button from the top right corner.

[[IMAGE: manual_img_091.jpg]]

- An Assign User dialog box pops up.

- Search for a user in the search bar by typing the username of the user.

- Click on the checkbox for the user to be assigned.

- Click on the Assign button.

[[IMAGE: manual_img_092.jpg]]

- A proper notification is thrown when the user is assigned successfully.

[[IMAGE: manual_img_093.jpg]]

Steps to de-assign user to the branch:

- From the action menu, click the De-assign button.

- A proper notification is thrown when the user is de-assigned successfully.

[[IMAGE: manual_img_094.jpg]]

### 6.3.2. Branch IPN List-View Details

[[IMAGE: manual_img_095.jpg]]

- Here we can view the list of IPNs assigned to the branch with their serial number. In the action menu, we can choose to view the details of IPN, and merchant assigned to the resp IPNs.

[[IMAGE: manual_img_096.jpg]]

Steps to assign IPN to the branch

- Click on the checkbox for an IPN or multiple IPNs from the available devices list to assign to the branch.

- If a specific IPN is required, search for the IPN to assign to a branch by entering the serial number in the search bar.

[[IMAGE: manual_img_097.jpg]]

- A user can also view the details of an IPN being assigned by clicking on the view details icon.

[[IMAGE: manual_img_098.jpg]]

[[IMAGE: manual_img_099.jpg]]

- Multiple IPNs can also be assigned.

[[IMAGE: manual_img_100.jpg]]

[[IMAGE: manual_img_101.png]]

Steps to de-assign IPN

- Click De-assign button from the action menu.

- When pop-up below appears, click on the De-assign button.

[[IMAGE: manual_img_102.jpg]]

[[IMAGE: manual_img_103.jpg]]

- The change is reflected in the system and the user is notified with a status message.

[[IMAGE: manual_img_104.png]]

### 6.3.3. Branch Merchant List-View Details

From the action menu, click on the view details button to get the details of the merchant assigned to the branch.

[[IMAGE: manual_img_105.jpg]]

[[IMAGE: manual_img_106.jpg]]

### 6.3.4. View details- Search section

The section box filters the user, IPN, and merchant information in their resp section only.

User section

[[IMAGE: manual_img_107.jpg]]

IPN section

[[IMAGE: manual_img_108.jpg]]

Merchant section

[[IMAGE: manual_img_109.jpg]]

## 6.4. Update Branch details

- Navigate to the Branch section.

- Click on the Edit branch option in the Actions tab for any Branch.

[[IMAGE: manual_img_110.jpg]]

[[IMAGE: manual_img_111.jpg]]

- Enter new details to be changed in the Update Branch dialog box.

- Click on the Update button.

- The branch is updated successfully, and the user is notified with a status message.

[[IMAGE: manual_img_112.jpg]]

## 6.5. Delete a branch

- Navigate to the Branch section,

- Click on the Delete option for a Branch.

[[IMAGE: manual_img_113.jpg]]

- A delete branch dialog box appears.

[[IMAGE: manual_img_114.jpg]]

- Click on the Delete button.

- The Branch is successfully deleted, and the change is reflected in the system. The user is notified with a status message.

[[IMAGE: manual_img_115.jpg]]

# 7. User

The "User" module offers a comprehensive solution for managing user access and adds a layer of security by limiting access to sensitive functionalities within the Koili TMS. Banks have the flexibility to create, view, update, and delete user profiles, allowing for the customization of roles and permissions. With seven distinct user roles – System Admin, Operator, Auditor, Checker, Branch Operator, IT operator and Partner – our bank clients can assign tailored responsibilities to individuals, ensuring a secure and controlled user environment.

• Navigate to the User Section on the left-side navigation menu, click on "User" under the Main section

[[IMAGE: manual_img_116.jpg]]

## 7.1. Add user

- On the User List page, locate and click the "ADD USER" button in the top-right corner to create a new user.

[[IMAGE: manual_img_117.jpg]]

- An Add User dialog box appears.

- Enter a new user’s details and select the role from dropdown.

[[IMAGE: manual_img_118.jpg]]

- After filling out the required fields:

- Click the "ADD" button to save the new user.

[[IMAGE: manual_img_119.jpg]]

- Click the “CANCEL” to discard changes.

[[IMAGE: manual_img_120.jpg]]

- The new user is created, and the admin user is notified with a status message.

User Guide: Setting Password

There are two methods to set or reset a user password in the TMS portal:

#### System-Generated Link

- After creating a user, the system generates a reset password link.

- The link is displayed as an Access Key (visible in a popup window).

- Steps:

  1. Copy the link using the "COPY TO CLIPBOARD" button.

  1. Share the link manually with the user (e.g., via chat or message).

  1. The user clicks the link to set their password.

[[IMAGE: manual_img_121.jpg]]

- Click on Copy to Clipboard button so that the link generated is copied automatically.

- Open a new tab on a browser and paste the copied link in the address bar of the browser and press enter. The user is redirected to the set password page.

[[IMAGE: manual_img_122.jpg]]

- Enter the password and confirm the password.

- Click on the Confirm password button.

[[IMAGE: manual_img_123.jpg]]

- A Confirm password dialog box appears. Click on the “YES” button.

[[IMAGE: manual_img_124.jpg]]

- The password is successfully set and the user is redirected to the Koili TMS portal.

[[IMAGE: manual_img_125.jpg]]

- Click the “NO” button, to discard the change.

[[IMAGE: manual_img_126.jpg]]

#### Email Reset Link

- The system automatically sends a password reset link to the user’s registered email address.

- Ensure the email address provided during user creation is correct.

- The user receives an email containing the reset link.

- The user clicks the link in the email to set their password.

## 7.3. View user details

- Click on the View user details option for any user from the action tab to view the details of the specific user.

[[IMAGE: manual_img_127.jpg]]

- A view user details dialog box appears.

- All the user information is displayed there.

[[IMAGE: manual_img_128.jpg]]

## 7.4. Update user details

- Click on the Edit User option for any user from the action tab.

[[IMAGE: manual_img_129.jpg]]

- An Update User dialog box appears.

- Edit the name or user role and click on the Update button.

[[IMAGE: manual_img_130.jpg]]

- The user is successfully updated.

- The change is reflected in the system and the user is notified with a status message.

[[IMAGE: manual_img_131.jpg]]

## 7.5. Reset password

- Click on the Reset password option from the Actions tab for a user to reset that user’s password.

[[IMAGE: manual_img_132.jpg]]

- A reset password dialog box appears. Click on the Reset button.

[[IMAGE: manual_img_133.jpg]]

- A reset password link is generated. This link is also sent via email to the user so they can reset the password themselves.

- Click on the Copy to Clipboard button to copy the link.

[[IMAGE: manual_img_134.jpg]]

- Open a new tab on a browser and paste the copied link in the address bar of the browser and press enter.

The user is redirected to the set password page.

- Enter the password and confirm the password.

- Click on the Confirm password button.

[[IMAGE: manual_img_135.jpg]]

- A Confirm password dialog box appears. Click on the Yes button.

[[IMAGE: manual_img_136.jpg]]

- The password is successfully reset, and the user is redirected to the Koili TMS portal.

[[IMAGE: manual_img_137.jpg]]

## 7.6. Delete user

- Click on the Delete option for a user in the action tab as shown.

[[IMAGE: manual_img_138.jpg]]

- A delete user dialog box appears. Click on the Delete button.

[[IMAGE: manual_img_139.jpg]]

- The user is successfully deleted. The change is reflected in the system and the user is notified with a status message.

[[IMAGE: manual_img_140.jpg]]

# 8. Scheme

The Scheme module in the Koili TMS portal enables precise identification and categorization of merchants and their associated IPNs. It facilitates seamless payment processing by allowing Payment Service Providers (PSPs) and Payment System Operators (PSOs) to effectively track and manage transactions. Scheme selection within the module involves choosing PSPs for specific merchants or IPNs, like Fonepay, NCHL, SCT etc. This functionality enhances flexibility and efficiency in the payment ecosystem, optimizing transaction routing for an improved payment experience.

• Navigate to the Scheme page by clicking on the Scheme option from the side navigation bar.

[[IMAGE: manual_img_141.jpg]]

## 8.1. Add Scheme

- Click on the Add Scheme button on the top right corner of the Scheme page.

[[IMAGE: manual_img_142.jpg]]

- An Add Scheme dialog box appears.

- Enter all the details of the required scheme.

[[IMAGE: manual_img_143.jpg]]

- The identifiers of the scheme need to be exactly as the identifiers provided by the respective PSP. The identifier field is case-sensitive. So, it needs to be entered with utmost care.

- The Label field is for the ease of the user and may be given to easily identify the identifier terms for the Merchant or the IPN.

- Click on the Add Entity button to add more identifiers if needed.

- Click on the Save button. Note that once the scheme is set and saved, the identifiers set can’t be edited, only new identifiers may be added. So utmost care is needed while entering scheme details. Double-check the identifiers entered before clicking on the Save button.

- The scheme is successfully saved. The change is reflected in the system and the user is notified with a status message

. [[IMAGE: manual_img_144.jpg]]

## 8.2. View Scheme details

- Click on the view details option by expanding the Actions tab for a Scheme.

[[IMAGE: manual_img_145.jpg]]

- A View Scheme details dialog box appears.

- The user can view the details of the selected scheme in the dialog box.

[[IMAGE: manual_img_146.jpg]]

## 8.3. Edit Scheme

- Click on the Edit option by expanding the Actions tab for a Scheme.

[[IMAGE: manual_img_147.jpg]]

- An update scheme dialog box appears.

[[IMAGE: manual_img_148.jpg]]

- Update the label values of the entities or add a new one by clicking on the Add Entity button.

- Then click on the Save button.

- The change is reflected only in the Scheme list and the user is notified about it with a status message.

[[IMAGE: manual_img_149.jpg]]

# 9. Partner

The Partner module within the Koili TMS portal facilitates efficient management of external entities collaborating with the system. This feature enables seamless handling of collaborating organizations, providing each entity with a dedicated dashboard within the TMS.

Partners, which include third-party organizations such as banks' clients, co-operatives, or finance companies, can access and manage their operations independently through a personalized interface within the TMS. With their own partner user profiles, partners can monitor and manage their merchants and Koili terminals without relying on the bank for access to the TMS portal. This capability empowers partners to oversee and control their operations effectively, enhancing autonomy and efficiency within the Koili ecosystem.

- Navigate to the Settings page.

- Enable the Partner toggle and click on Apply Settings.

[[IMAGE: manual_img_150.jpg]]

- Click on Apply button on the Confirm Settings dialog box. The page refreshes and the Partner section is now enabled in the system.

[[IMAGE: manual_img_151.jpg]]

- Navigate to the Partner page by clicking on the Partner option from the side navigation bar.

[[IMAGE: manual_img_152.jpg]]

## 9.1 Add Partner

- Click on the Add Partner button in the top right corner in the Partner page.

[[IMAGE: manual_img_153.jpg]]

- An add partner dialog box appears.

[[IMAGE: manual_img_154.jpg]]

- Enter valid Partner details. Note that the subscription key must be a valid unique value.

- Partners won’t be able to sync the IPNs without a valid subscription id.

- Partners have their own domain name that partner users can use to log in to their dashboard. The domain name also needs to be unique and must be in a valid URL format.

- Click on the Add button.

[[IMAGE: manual_img_155.jpg]]

- The Partner is successfully added.

The user is notified about it with a status message and the change is reflected in the partner list.

[[IMAGE: manual_img_156.jpg]]

## 9.2 View Partner Details

- Click on the View details option by expanding the Action tab for a Partner.

[[IMAGE: manual_img_157.jpg]]

- A View Partner details dialog box appears with the partner details.

[[IMAGE: manual_img_158.jpg]]

## 9.3 View Partner Users

- Click on the Partner Users option for any partner.

[[IMAGE: manual_img_159.jpg]]

- The user is redirected to a page with a Partner Users list where the users of a specific partner can be viewed.

[[IMAGE: manual_img_160.jpg]]

## 9.4 Assign User to a Partner

- Click on the Partner Users option for a partner.

- Click on the Assign User button.

- An Assign User dialog box appears.

[[IMAGE: manual_img_161.jpg]]

- Search for a partner user by entering their username in the search bar.

- Click on the checkbox for the partner user listed.

[[IMAGE: manual_img_162.jpg]]

- Click on the Assign button.

- The partner user is successfully assigned.

- The user is notified about it with a status message and the change is reflected in the partner users list.

[[IMAGE: manual_img_163.jpg]]

## 9.5 De-assign Partner User

- Navigate to the Users list of a partner by clicking on Partner Users option from the Actions tab for a partner.

- Click on the De-assign option by expanding the Actions tab for a partner user.

- A De-assign User confirmation box appears.

[[IMAGE: manual_img_164.jpg]]

[[IMAGE: manual_img_165.jpg]]

- Click on the De-Assign button.

- The partner role user is successfully de-assigned from the selected partner.

- The user is notified about it with a status message and the change is reflected in the Portal.

[[IMAGE: manual_img_166.jpg]]

## 9.6 Update Partner

- Click on the Edit option by expanding the Action tab for any Partner.

[[IMAGE: manual_img_167.jpg]]

- An update partner dialog box appears.

[[IMAGE: manual_img_168.jpg]]

- Update the required details of the Partner. Note that care should be taken if updating the subscription ID of a partner as it is required to sync the IPNs assigned to a partner. Only the IPNs assigned to the specific subscription ID can be synced. Updating the domain name of a partner should also be done with care and the domain name should be in a valid URL format.

- Click on the Update button.

- The partner is successfully updated.

- The change is reflected in the system and the user is notified about it with a status message.

[[IMAGE: manual_img_169.jpg]]

## 9.7 Delete Partner

- Click on the Delete option for a Partner in the partner list.

- A Delete Partner dialog box appears.

[[IMAGE: manual_img_170.jpg]] [[IMAGE: manual_img_171.jpg]]

- Click on the Delete icon. Note that there may be errors if a partner is deleted if the IPNs are already synced.

- The partner is successfully deleted.

- The change is reflected in the system and the user is notified about it with a dialog box.

[[IMAGE: manual_img_172.jpg]]

# 10. Merchant

In the "Merchant" section, banks can oversee and manipulate merchant details efficiently. CRUD operations for merchants enable clients to add, modify, and remove merchant information as needed. This functionality ensures that our clients can maintain an up-to-date and organized portfolio of merchants associated with their IPN ecosystem.

• Navigate to the Merchant section by clicking on the Merchant option in the side navigation bar.

[[IMAGE: manual_img_173.jpg]]

## 10.1. Add Merchant

- Click on the Add Merchant button in the top-right corner of the Merchant page.

[[IMAGE: manual_img_174.jpg]]

- An Add Merchant Window box appears.

- Enter the details of the Merchant to be onboarded. The Account number, Merchant PAN, Merchant identifiers for the scheme, Email and Phone number needs to be unique for each Merchant. Branch must be selected for the Merchant to be onboarded to a specific branch from the drop-down menu or search by typing the branch name in the field.

- Click on “ADD” button.

[[IMAGE: manual_img_175.jpg]]

- The Merchant creation request is successfully sent for approval.

- The request is listed in the Operation section and the user is notified about it with a status message.

[[IMAGE: manual_img_176.jpg]]

## 10.2. View Merchant Details

- A user can view the details of a Merchant by clicking on the View Details option by expanding the Actions tab for a Merchant.

- A View Merchant Details dialog box appears.

- The user can view the details of the Merchant in the dialog box.

[[IMAGE: manual_img_177.jpg]]

- A View Merchant Windows appears.

- The user can view the details of merchant on the window screen.

[[IMAGE: manual_img_178.jpg]]

## 10.3. View Assigned IPNs of a Merchant

- Click on the Assigned IPNs option for a Merchant from the Actions tab.

[[IMAGE: manual_img_179.jpg]]

- The user is then redirected to the Assigned IPNs list for the Merchant.

- The user can thus view the list of the IPNs of the selected Merchant.

[[IMAGE: manual_img_180.jpg]]

## 10.4. Assign IPN to a Merchant

- To Assign an IPN to a Merchant, the user first needs to navigate to the Assigned IPNs list of the Merchant by clicking on the Assigned IPNs option for a Merchant.

•

[[IMAGE: manual_img_181.jpg]]

- Click on the Assign IPN button.

[[IMAGE: manual_img_182.jpg]]

- An Assign IPN page appears.

[[IMAGE: manual_img_183.jpg]]

- Click on the checkbox of an IPN to select an IPN from the available IPNs from the list displayed.

- If a specific IPN is required, enter the serial number of an IPN in the search box to assign to the Merchant and click on the checkbox.

[[IMAGE: manual_img_184.png]]

- Click on the scheme icon next to the listed IPN from the Actions tab.

- A scheme dialog box appears.

[[IMAGE: manual_img_185.jpg]]

- Enter the scheme identifier values for the IPN selected. The scheme identifier values for the IPN needs to be unique from other IPNs.

[[IMAGE: manual_img_186.jpg]]

- Click on the update button.

- The scheme is thus set for the IPN, and the user is notified about it through a status message.

- Then, click on the Next button.

- Click on Assign button.

- The IPN assign request is successfully sent for approval. The user is notified about it with a status message.

[[IMAGE: manual_img_187.jpg]]

[[IMAGE: manual_img_188.jpg]]

- The request sent needs to be verified and approved by a checker or the system admin user if the auto approval is off, in this case auto approval is off, so the IPN assigned to merchant automatically.

- Navigate to the Approval section in the checker’s dashboard or the operation section of admin in case if the auto approval is on.

[[IMAGE: manual_img_189.jpg]]

- Here you can choose to view details, approve or deny.

- In case of approval

[[IMAGE: manual_img_190.jpg]]

- Click on the Approve button. Verify remarks aren’t mandatory.

- The request is successfully approved, and the user is notified about it through a status message and the change is reflected in the Merchant list.

[[IMAGE: manual_img_191.jpg]]

- The user can check this by clicking on the Assigned IPNs option for the respective Merchant.

[[IMAGE: manual_img_192.jpg]]

[[IMAGE: manual_img_193.jpg]]

## 10.5. De-assign IPN from a Merchant

- Navigate to the Assigned IPN list of a Merchant by clicking the Assigned IPNs option for a Merchant.

[[IMAGE: manual_img_194.jpg]]

- Click on the De-assign IPN option for any IPN to be de-assigned.

- A De-assign IPN dialog box appears.

[[IMAGE: manual_img_195.jpg]]

- Click on the De-assign button.

- An IPN de-assign dialog box appears.

- Click on the De-assign button.

- The IPN de-assign request is sent for approval.

- The user is notified about this with a status message.

[[IMAGE: manual_img_196.jpg]]

[[IMAGE: manual_img_197.jpg]]

- The request sent needs to be verified and approved by a checker or the system admin user.

- Navigate to the Approval section in the checker’s dashboard.

- Click on the Approve option for the IPN de-assign request made.

[[IMAGE: manual_img_198.jpg]]

- An approve dialog box appears.

- Click on the Approve button.

- The request is approved, and the change is reflected in the Merchant. The user is also notified with a status message.

[[IMAGE: manual_img_199.jpg]]

[[IMAGE: manual_img_200.jpg]]

## 10.6. Update Merchant

- Click on the Edit option under the Actions tab on the Merchant List Page.

[[IMAGE: manual_img_201.jpg]]

- An Update Merchant dialog box appears.

- Update the required Merchant details and click on the Update icon.

[[IMAGE: manual_img_202.jpg]]

- The Merchant update request is sent for approval and the user is notified about this through a status message.

[[IMAGE: manual_img_203.jpg]]

- The request sent needs to be verified and approved by a checker or the system adminuser.

- Navigate to the Approval section in the checker’s dashboard.

- Click on the View details option by expanding the Actions tab for the Merchant update request to verify details.

[[IMAGE: manual_img_204.jpg]]

- The Request details dialog box appears.

- Click on the downward arrow to view a detailed changed view of the request.

[[IMAGE: manual_img_205.jpg]]

- Close the Request details dialog box and click on the approve icon for the request.

- Click on the Approve option for the Merchant update request made.

[[IMAGE: manual_img_206.jpg]]

- An approve dialog box appears.

- Click on the Approve button.

[[IMAGE: manual_img_207.jpg]]

- The request is approved and the change is reflected in the Merchant. The user is also notified with a status message.

[[IMAGE: manual_img_208.jpg]]

## 10.7. Delete Merchant

- Click on the Delete option by expanding the Actions tab for a Merchant.

[[IMAGE: manual_img_209.jpg]]

- A delete Merchant dialog box appears.

- Click on the Delete icon.

- The Merchant delete request is sent for approval and the user is notified about this through a status message.

The user isn’t allowed to perform any other operations on the Merchant when the Merchant is already on audit.

[[IMAGE: manual_img_210.jpg]]

[[IMAGE: manual_img_211.jpg]]

- The request sent needs to be verified and approved by a checker or the system admin user.

- Navigate to the Approval section in the checker’s dashboard.

- Click on the view details option for the Merchant update request to verify details.

[[IMAGE: manual_img_212.jpg]]

- The Request details dialog box appears.

- Click on the downward arrow to view a detailed changed view of the request.

[[IMAGE: manual_img_213.jpg]]

- Close the Request details dialog box.

- Click on the Approve option for the Merchant update request made.

[[IMAGE: manual_img_214.jpg]]

- An approve dialog box appears.

- Click on the Approve button.

- The request is approved and the change is reflected in the Merchant. The user is also notified with a status message.

## 10.8. Operation in Merchant

- A user can view all the requests made, approved, and denied for a Merchant using the operation button.

- Click on the Operation button.

[[IMAGE: manual_img_215.jpg]]

- There are three statuses that a user can select to view the operation requests accordingly: pending, approved, and denied.

[[IMAGE: manual_img_216.jpg]]

## 10.9. Sorting in Merchant Table

- The Merchant Module now supports Multi-Criteria Sorting, allowing users to sort data by multiple fields in a prioritized sequence. Navigate to Merchant from the sidebar.

- Click on any column header (e.g., Name) to sort in ascending (↑) or descending (↓) order.

[[IMAGE: manual_img_217.jpg]]

- Add Additional Sorting Criteria.

- Sortable columns show an arrow (↑ or ↓).

[[IMAGE: manual_img_218.jpg]]

Reset Sorting

- Click on any column header 3 times to reset sorting and return to the default view.

[[IMAGE: manual_img_219.jpg]]

- Click on “BRANCH” filter button, to filter branch-specific management.

[[IMAGE: manual_img_220.jpg]]

- Enter branch name on search bar or Select from drop down.

[[IMAGE: manual_img_221.jpg]]

- The Merchant list are displayed by branch wise.

[[IMAGE: manual_img_222.jpg]]

## 10.10. Export Merchant details

- Click on “EXPORT” button on the top right corner of the Merchant page, to export the Merchant data.

[[IMAGE: manual_img_223.jpg]]

- Click on the Export button on the top right corner of the Merchant page.

[[IMAGE: manual_img_224.jpg]]

- If Merchant details of all Branch and with their IPN details are required, turn on the toggles and click on Export button. An excel file with all the details will then be downloaded.

- The user can also choose specific branches for which the merchant details are required and export those details accordingly.

[[IMAGE: manual_img_225.jpg]]

# 11. IPN

The IPN feature within the TMS provides a comprehensive overview of all IPN devices synced from the core registry into the TMS portal. This section offers functionalities to edit IPN details, view IPN operations, and initiate synchronization of IPN devices through a dedicated "Sync IPN" button. This feature empowers administrators to seamlessly manage IPN devices within the TMS, ensuring they remain up to date-for optimal performance. Overall, the IPN feature enhances operational efficiency and streamlines device management within the TMS, facilitating smooth and effective administration of the IPN ecosystem.

• Navigate to the IPN section by clicking on the IPN option from the side navigation bar.

[[IMAGE: manual_img_226.jpg]]

## 11.1 Sync IPN

- Click on the Sync IPN button on the top-right corner of the IPN page.

[[IMAGE: manual_img_227.jpg]]

- The user is notified about the IPNs being synced from the core registry with a status message.

- In case new devices are synced, the user will get a status message that reads “IPNs

- added successfully” or if no new devices are added, the user will get a status message “everything is up to date”.

[[IMAGE: manual_img_228.jpg]]

## 11.2 View IPN details

- Click on the View details option by expanding the Action tab for any IPN.

- A View IPN details dialog box appears where a user can view details of the IPN.

[[IMAGE: manual_img_229.jpg]]

- If an IPN is assigned to a Merchant, users can also view the details of the Merchant the IPN is assigned to in the View IPN details dialog box.

- Click on the downward arrow in the Merchant detail tab in the View IPN details dialog box to view the

Merchant details.

[[IMAGE: manual_img_230.jpg]]

## 11.3 Update IPN

- Click on the Edit option by expanding the Actions tab for an IPN.

[[IMAGE: manual_img_231.jpg]]

- An Update IPN dialog box appears.

- Update the required IPN details.

- Click on Update icon.

[[IMAGE: manual_img_232.jpg]]

- The IPN update request is sent for approval.

- The user is notified about it through a status message. The user cannot make any more updates on the IPN before approval of the previous request which is denoted by the greying out of the update icon for the IPN.

[[IMAGE: manual_img_233.jpg]]

[[IMAGE: manual_img_234.jpg]]

- The request sent needs to be verified and approved by a checker or the system admin user.

- Navigate to the Approval/Operation section in the checker/admin’s dashboard.

- Click on the view details option for the IPN update request to verify details.

[[IMAGE: manual_img_235.jpg]]

- The Request details dialog box appears.

- Click on the downward arrow to view detailed changed view of the request.

[[IMAGE: manual_img_236.jpg]]

- Close the Request details dialog box and click on approve icon for the request.

- An approve dialog box appears.

- Click on Approve button.

[[IMAGE: manual_img_237.jpg]]

[[IMAGE: manual_img_238.jpg]]

- The request is approved, and the change is reflected in the IPN. The user is also notified with a status message.

[[IMAGE: manual_img_239.jpg]]

## 11.4 Sorting in IPN Table

- The IPN Module now supports Multi-Criteria Sorting, allowing users to sort data by multiple fields in a prioritized sequence. Navigate to IPN from the sidebar.

- Click on any column header (e.g., Serial Number ) to sort in ascending (↑) or descending (↓) order.

[[IMAGE: manual_img_240.jpg]]

- IPNs can also be filtered by branch and status. Users can now see the status of IPNs in the Assigned column. A checkbox indicates whether an IPN is assigned (checked) or not (unchecked). Users can filter the IPN list based on the assigned status.

[[IMAGE: manual_img_241.jpg]]

[[IMAGE: manual_img_242.jpg]]

- User can also set the number of IPN to be visible in the page by using the pagination feature. (for: instead of 10 IPN, users can view 25 IPNs list in the same page)

[[IMAGE: manual_img_243.jpg]]

# 12. Settings

The Settings page of the Koili TMS portal offers an advanced solution for managing API keys and Email Configuration, enhancing the system's functionality and security.

## 12.1. API Key

Within the Settings module, banks can generate API keys and securely share them with clients (PSPs) for authentication and authorization purposes. These API keys serve as unique identifiers, establishing a secure handshake between the

Terminal Management System and a discovery API. By facilitating secure authentication and authorization processes, API keys ensure seamless integration between different components of the system, enhancing overall efficiency and security.

- Navigate to the Settings section by clicking on Settings option from the side navigation bar.

[[IMAGE: manual_img_244.jpg]]

- Click on the API keys widget.

[[IMAGE: manual_img_245.jpg]]

- The user is redirected to the API keys page.

- Click on the Generate API key button on the top-right corner.

[[IMAGE: manual_img_246.jpg]]

## 12.2. Email configuration

Banks have the flexibility to configure SMTP settings within the Settings module, allowing for customization of email communication based on their specific requirements. This feature enables users to receive emails when a new user is added with a different role for the first time in the Koili TMS portal. Additionally, users can easily set their passwords during initial role assignment, thereby enhancing the overall user experience. Password reset links sent via email further ensure secure password recovery procedures, maintaining the integrity and security of user accounts within the system.

- Navigate to the Settings section by clicking on Settings option from the side navigation bar.

[[IMAGE: manual_img_247.jpg]]

- Click on the Email Config widget.

- The user is redirected to the Email config page.

[[IMAGE: manual_img_248.jpg]]

- Click on the Edit button.

[[IMAGE: manual_img_249.jpg]]

- Enter the SMTP email configuration details.

- Click on update button.

[[IMAGE: manual_img_250.jpg]]

- The Email SMTP configuration is successful, and the user is notified about it with a status message.

[[IMAGE: manual_img_251.jpg]]

## 12.3 Billing toggle

There are two billing configurations available: Pumari (Manual) and Finacle (Automated). Having separate configurations for manual and automated billing ("Pumari" and "Finacle") adds flexibility for different business needs.

Here are user guide steps to configure billing.

- To activate the billing module, Click on the Setting menu on left hand side bar

[[IMAGE: manual_img_252.png]]

- Locate to the Billing toggle button, click the toggle button to enable it.

- Click the “Apply Settings” button.

[[IMAGE: manual_img_253.png]]

- Click on “Apply” button to save the settings.

[[IMAGE: manual_img_254.jpg]]

- A new billing widget in the settings page redirects users to the billing setup page.

[[IMAGE: manual_img_255.jpg]]

- An account journal button also appears for advanced accounting.

[[IMAGE: manual_img_256.jpg]]

### 12.3.1 Configuring Pumari Billing Setup

This guide provides step-by-step instructions to configure the Pumari Billing Setup with Advanced Accounting and Parking Details. Upon applying the settings, an Account Journal Module will appear under the Campaign section.

The default income and payable account journal fields must be populated accordingly.

- To Configure Pumari Billing setup in the Billing Setup panel, locate the Scheme dropdown and Select Scheme "Pumari".

[[IMAGE: manual_img_257.jpg]]

- Toggle the Advanced Accounting switch to enable it (switch will turn blue).

[[IMAGE: manual_img_258.jpg]]

- Enter “Bank, Account number and Name” to configure Parking details.

[[IMAGE: manual_img_259.jpg]]

Here, If this is the first-time billing configuration, the Default Journals fields can be skipped. (Optional for First-

Time Setup)

[[IMAGE: manual_img_260.jpg]]

- Click on the "APPLY SETTINGS" button.

[[IMAGE: manual_img_261.jpg]]

- Once settings are applied, Account Journal appears on the left-hand menu.

- The Billing-Account Journal section integrates the billing process of bank’s financial accounting system. It helps in managing and viewing all account journals within the system.

*Account journal button appears only when billing is enabled. Guide to enable the billing feature is above.

[[IMAGE: manual_img_262.jpg]]

### 12.3.2 Add Journal

- Click on “ADD JOURNAL” button locate at the Billing setup page.

[[IMAGE: manual_img_263.jpg]]

- A window appears to add account journal.

- Select the Account Type and enter the account number.

[[IMAGE: manual_img_264.jpg]]

- Click one “ADD” button to save the journal.

[[IMAGE: manual_img_265.jpg]]

- Wait for the confirmation Message.

[[IMAGE: manual_img_266.jpg]]

### 12.3.3 Set Default Account Journals in Billing Setup

- Navigate to the Billing setup page, Select the Account Journal you created.

[[IMAGE: manual_img_267.jpg]]

- Click on “APPLY” button to save the configuration.

[[IMAGE: manual_img_268.jpg]]

### 12.3.4 Configuring Finnacle Billing Setup

This guide provides step-by-step instructions to automate billing using the Finnacle scheme configuration in the portal.

- To Configure Pumari Billing setup in the Billing Setup panel, locate the Scheme dropdown and Select Scheme "Finnacle".

- The Core Banking System (CBS) toggle will automatically enable (turn blue).

[[IMAGE: manual_img_269.jpg]]

- Toggle the Advanced Accounting switch to enable additional accounting features (switch turns blue).

Enter the Input CBS Integration Details, Import Private Certificate, and Configure Parking Details

[[IMAGE: manual_img_270.jpg]]

- Click on “APPLY SETTING” button to save configuration.

[[IMAGE: manual_img_271.jpg]]

### 12.3.5 Billing Setup-Plan

This guide explains how to view the list of plans that are fetched from the Core System.

- Navigate to the Billing setup page.

[[IMAGE: manual_img_272.jpg]]

- Click on “Plan” to view the Plan List.

[[IMAGE: manual_img_273.jpg]]

- Click on “View details” under the Action to view individual Plan details.

[[IMAGE: manual_img_274.jpg]]

A window with plan details appears.

[[IMAGE: manual_img_275.jpg]]

- Click on “Plan IPNs” under the Action to view IPN list associated with individual plans.

[[IMAGE: manual_img_276.jpg]]

- A window with IPN list appears.

[[IMAGE: manual_img_277.jpg]]

- Click on “ASSING IPN” button to assign IPN to Plan.

[[IMAGE: manual_img_278.jpg]]

- A window for IPN assignment appears.

- Enter serial number on search bar and select the IPN • Click on “Assign” button.

[[IMAGE: manual_img_279.jpg]]

- Click on “View Details” button under the action to view the details of IPN.

[[IMAGE: manual_img_280.jpg]]

Click on “Des-assign” button under the action to de-assign device from Plan.

[[IMAGE: manual_img_281.jpg]]

- A dialog box appears to confirm the de-assign.

- Click on “DE-ASSIGN” button to continue the change.

[[IMAGE: manual_img_282.jpg]]

- Click on “CANCEL” button to discarded the change.

[[IMAGE: manual_img_283.jpg]]

### 12.3.6 Billing Setup-Campaign

- Navigate to the billing setup page, to view Campaign list.

- Click on “Campaign”

[[IMAGE: manual_img_284.jpg]]

- User redirected to the campaign list page.

[[IMAGE: manual_img_285.jpg]]

- Click on “View details” tab under the action to view individual Campaign.

[[IMAGE: manual_img_286.jpg]]

  1. window with campaign details appears.

[[IMAGE: manual_img_287.jpg]]

- Click on “campaign IPNs” list under the Action to view IPNs associated with campaign.

[[IMAGE: manual_img_288.jpg]]

- Campaign IPNs list page

[[IMAGE: manual_img_289.jpg]]

Click on “ASSIGN IPN” button to assign IPN to campaign.

[[IMAGE: manual_img_290.jpg]]

- A window for IPN assignment appears.

- Enter serial number on search bar and select the IPN • Click on “Assign” button.

[[IMAGE: manual_img_291.jpg]]

### 12.3.7. Add Campaign

- Click on “ADD CAMPAIGN” button to add campaign.

[[IMAGE: manual_img_292.jpg]]

  1. window for “Add Campaign” appears

[[IMAGE: manual_img_293.jpg]]

- Fill the “Add Campaign” fields.

- Click on “ADD” button.

[[IMAGE: manual_img_294.jpg]]

## 12.4. Auto-Approval toggle

The Auto-Approval Toggle feature introduces a new level of flexibility and customization to the Koili TMS portal. Found within the Settings page, users now have access to a toggle button that enables or disables autoapproval feature that let users perform operations without waiting for their requests to be approved. Any changes users make are thus instantly reflected in the system.

• Navigate to the Settings section by clicking on the Settings option from the side navigation bar.

[[IMAGE: manual_img_295.jpg]]

However, when the Auto-Approval toggle is on, branch operators and operators can easily perform operations under Merchant and IPN without their request being sent for approval. The changes made in the system are instantly reflected speeding the workflow.

[[IMAGE: manual_img_296.jpg]]

However, when the Auto-Approval toggle is off, users such as operators and branch operators have to create request for all operations performed under Merchant and IPN and wait for them to be approved by a Checker user or the System Admin.

To turn on the Auto-Approval feature,

- Click on the Auto-Approval toggle button when the button is turned off.

- Click on Apply settings button.

- Click on Apply button in the confirmation dialog box. The site is automatically refreshed, and all

operations done by users are instantly reflected in the system without the need for approval.

[[IMAGE: manual_img_297.jpg]] [[IMAGE: manual_img_298.jpg]]

To turn off the Auto-Approval feature:

- Click on the Auto-Approval toggle button when the button is turned on.

- Click on Apply settings button.

Click on Apply button in the confirmation dialog box. The site is automatically refreshed, and all the operations performed by the users are sent for approval by a Checker user or the System admin before being reflected in the system.

[[IMAGE: manual_img_299.jpg]] [[IMAGE: manual_img_300.jpg]]

## 12.5 Partner toggle

The Partner Toggle feature introduces a new level of flexibility and customization to the Koili TMS portal. Found within the Settings page, users now have access to a toggle button that enables or disables partnerrelated functions and features. Users can thus seamlessly tailor the portal to their specific needs, either unlocking partner-related features or limiting access as required.

• Navigate to the Settings section by clicking on the Settings option from the side navigation bar.

[[IMAGE: manual_img_301.jpg]]

[[IMAGE: manual_img_302.jpg]]

Note that the Partner feature toggle is turned off in the diagram above and similarly, partner- related sections are unavailable in the side navigation bar as well. Partner role users are also unavailable in the User list in the User section of the profile.

To turn on the Partner feature,

- Click on the Partner toggle button when the button is turned off.

- Click on Apply settings button.

- Click on Apply button in the confirmation dialog box. The site is automatically refreshed, and the partner-related sections are available in the side navigation bar.

[[IMAGE: manual_img_303.jpg]]

[[IMAGE: manual_img_304.jpg]]

[[IMAGE: manual_img_305.jpg]]

To turn off the Partner feature,

- Click on the Partner toggle button when the button is turned on.

- Click on Apply settings button.

- Click on Apply button in the confirmation dialog box. The site is automatically refreshed and the partner-related sections are removed from the side navigation bar.

[[IMAGE: manual_img_306.jpg]]

[[IMAGE: manual_img_307.jpg]]

[[IMAGE: manual_img_308.jpg]]

# 13. Audit Log

The Audit Log section of the Koili TMS portal serves as a comprehensive repository of all user activities and system events. This includes logs of operations performed by users, login/logout information, and changes made in Merchant/IPN, branch, partner, and other sections of the system. Essentially, the Audit Log provides a chronological record of events and changes within the system, offering users valuable insights into system activities.

● Navigate to the Audit log section by clicking on Audit log option from the side navigation bar.

[[IMAGE: manual_img_309.jpg]]

## 13.1. Time filter

The time range selection is further refined, allowing users to choose a maximum time span of 3 months at a time to display logs. Users can specify time intervals by selecting AM or PM and hourly times, enabling them to narrow down their search to 1-hour intervals.

Additionally, if only the “from time” filter is selected without specifying the “to time” filter, the system retrieves logs from the chosen date and time up to the present moment, providing users with real-time updates on system activities.

- Click on the date selection button for the “from time” tab.

- Enter a date to display the audit logs from.

[[IMAGE: manual_img_310.jpg]]

- Click on the date selection icon in the “To Time” tab.

- Enter a date and time for the “to time” limit. The “to time” filter must be greater than “from time” filter, otherwise the dates isn’t accepted.

[[IMAGE: manual_img_311.jpg]]

- Click on Search button.

- The Audit logs of the chosen time range are then displayed.

[[IMAGE: manual_img_312.jpg]]

## 13.2. View Log Details

- A user can view the details of any of the Audit logs recorded by clicking on the View Details option by expanding the Actions tab for any audit log displayed.

[[IMAGE: manual_img_313.jpg]]

- The Log Details dialog box appears.

- Click on the downward arrow to view detailed changed view. The detailed view contains all the relevant information of the log made.

[[IMAGE: manual_img_314.jpg]]

# 14. Bill

## 14.1. Create bill

The Create Bill feature enables users to generate a new billing entry for a selected merchant. This functionality allows for the specification of various billing details, such as merchant information, billing period, commission, discount, and rate. The Create Bill form is designed to be user-friendly, with options to add individual devices and automatically calculate the total amounts.

Steps to create bill using campaigns:

Campaigns are applied to the existing default plan.

- Add a merchant and assign IPN following the steps below.

[[IMAGE: manual_img_315.jpg]]

[[IMAGE: manual_img_316.jpg]]

[[IMAGE: manual_img_317.jpg]]

[[IMAGE: manual_img_318.jpg]]

- Navigate to the settings and select the billing option.

[[IMAGE: manual_img_319.jpg]]

- Go to the Campaign section in the billing setup page.

[[IMAGE: manual_img_320.jpg]]

- There is a list of campaign option. Each campaign provides different offers. Choose any one of them and from the action menu click the Campaign IPNs button.

[[IMAGE: manual_img_321.jpg]]

- Once the Assign IPN dialog box appears, enter the serial number of the IPN added to the merchant in a previously selected campaign to assign device in the resp campaign.

[[IMAGE: manual_img_322.jpg]]

- Once the device is assigned, user is notified with the notification.

[[IMAGE: manual_img_323.jpg]]

- Here, user can also create the campaign plan according to the bank’s need.

[[IMAGE: manual_img_324.jpg]]

- Add the commission. Discount and fixed deposit amount according to the plan scheme and click add.

[[IMAGE: manual_img_325.jpg]]

- Now, we can successfully create a bill.

- Click on the Create Bill option.

[[IMAGE: manual_img_326.jpg]]

- Enter the account no or pan no or name of the merchant and specify the time periods. Once the device information is retrieved, System automatically calculates total amount. Then, click the save button.

[[IMAGE: manual_img_327.jpg]]

- Once we save the bill, it is saved as a draft. We can view details, edit or delete.

- To confirm payment, click the view details option.

[[IMAGE: manual_img_328.jpg]]

- Click the confirm payment button to successfully verify payment.

[[IMAGE: manual_img_329.jpg]]

- Enter the transaction code and click confirm.

[[IMAGE: manual_img_330.jpg]]

- Once the payment is confirmed, user is notified with the notification.

[[IMAGE: manual_img_331.jpg]]

Additional verification: To check if the payment is confirmed: Navigate to the billing> bill history section.

[[IMAGE: manual_img_332.jpg]]

### 14.1.1. Create bill with default setting

1. Navigate to the billing> Create bill.

1. Enter the ipn assigned merchant name that you want to create bill for.

For example: Prachi (as shown below)

[[IMAGE: manual_img_333.jpg]]

Click the save button.

After clicking the save button, the bill will be saved in a draft state as shown below

[[IMAGE: manual_img_334.jpg]]

From the action menu, click the view details button.

[[IMAGE: manual_img_335.jpg]]

Click on the confirm payment button. Right after that, click confirm button from the displayed confirm dialog box

[[IMAGE: manual_img_336.jpg]]

If you don’t want to continue the payment, click the cross(x) button on top right corner of the dialog box or else, click confirm.

[[IMAGE: manual_img_337.jpg]]

Here, we can see that the bill of the merchant named “Prachi” is saved in a paid state i.e. bill is successfully created.

[[IMAGE: manual_img_338.jpg]]

## 14.2. Bulk verification

The system has the option to verify the draft/in-queue bills in bulk without having to manually enter and confirm payment of each merchant.

To Bulk verify:

- Click the Bulk verify button.

[[IMAGE: manual_img_339.jpg]]

- Click confirm button to bulk verify.

[[IMAGE: manual_img_340.jpg]]

- Observe the result as seen in the picture below.

[[IMAGE: manual_img_341.jpg]]

## 14.3. BILL HISTORY

The Billing History page provides an overview of all billing records, including details for each transaction such as merchant information, date range, serial number, total amount, and timestamps. This feature allows users to track and manage billing records efficiently.

Navigating to Billing History

1. From the Dashboard main menu, scroll down to the Billing section.

1. Click on Bill History to access the page.

[[IMAGE: manual_img_342.jpg]]

## 14.4. Export Data

The export data button on the right corner downloads the entire billing history list as an Excel file, making it convenient for offline analysis or record-keeping.

To export the billing history data:

Steps to Export Billing History:

1. Navigate to the Billing History Page:

• Go to Billing > Bill History from the main menu on the left side of the dashboard.

2. Click on the Export Excel Button:

• On the Billing History page, click on the Export Excel button located at the top right corner of the page.

3. Select Year and Month:

- An Export Excel dialog box will appear with dropdown menus to filter the data by Year and Month.

- Click on the Year dropdown to select the desired year for the export.

- Click on the Month dropdown to select the desired month. If you want to export data for the entire year, leave the month field blank.

- After selecting the filters, confirm your choice by clicking on the Export button.

- The system will generate an Excel file with the filtered billing records, which will automatically download to your device.

[[IMAGE: manual_img_343.jpg]]

[[IMAGE: manual_img_344.jpg]]

[[IMAGE: manual_img_345.jpg]]

# 15. Profile

The Profile module within the TMS portal offers users a personalized space to access and manage essential information. Users can conveniently view details such as username, email, first name, last name, and role within the Koili TMS, ensuring easy access to key user information.

- Navigate to the Profile section by clicking on the Profile option from the side navigation bar.

[[IMAGE: manual_img_346.jpg]]

- The user can view User information in the Profile section. The username, email, first name, last name and role of the user is displayed.

[[IMAGE: manual_img_347.jpg]]

## 15.1. Change Password

The "Change Password" feature empowers users to maintain the security of their accounts by easily updating their passwords as needed. This feature ensures a secure and personalized login experience, enhancing overall account security within the TMS.

- Click on the Change password button.

- A Change password dialog box appears.

[[IMAGE: manual_img_348.jpg]]

- Enter current password and new password.

- Enter new password again for confirmation.

- Click on Change password button.

- The password is then successfully changed, and the user is redirected to the login page.

[[IMAGE: manual_img_349.jpg]]

## 15.2. Notify Checker

Additionally, the Profile module includes a unique "Notify Checker" section, which introduces an innovative approach to request review and workflow management. Users can add a checker role user in the Notify Checker section, assigning them to review requests created by the user. The checker user can access these requests by switching the toggle to "My approvals." Moreover, users have the flexibility to remove the checker from the Notify Checker section as needed.

The Notify Checker feature adds a layer of accountability to the request review process, streamlining workflow management and enhancing transparency within the TMS. Overall, the Profile module provides users with the tools and features necessary to manage their account information effectively and optimize workflow processes within the TMS portal.

Navigate to the Notify Checker section in the Profile section of the user dashboard in TMS portal.

[[IMAGE: manual_img_350.jpg]]

### 15.2.1. Add Checker To add checker:

- Click on Add Checker button in the Notify Checker section.

[[IMAGE: manual_img_351.jpg]]

- An Add Checker dialog box appears.

[[IMAGE: manual_img_352.jpg]]

- Enter the username of a checker role user in the search bar.

- The user is listed in the list below.

- Click on the checkbox to select the checker user.

- Click on Add button.

[[IMAGE: manual_img_353.jpg]]

- The selected checker is then added to the Notify Checker section.

- The user is notified about it with a status message.

- The checker is listed in the Notify Checker section list. All the operation requests now made will be assigned to that checker specifically as well.

[[IMAGE: manual_img_354.jpg]]

### 15.2.2 Remove Checker

A checker added in the Notify Checker section can be removed as well.

- Click on the Remove option by expanding the Actions tab for the checker in the Notify Checker section.

- A Remove Checker dialog box appears.

[[IMAGE: manual_img_355.jpg]]

[[IMAGE: manual_img_356.jpg]]

- Click on the Remove button.

- The checker is removed from the list and the user is notified about it with a status message.

[[IMAGE: manual_img_357.jpg]]

# 16. Logout

A user can logout of the Koili TMS portal by 2 methods:

1. Logout option from the side navigation bar.

1. Logout button from the Profile icon in the top-right corner of the user dashboard.

From side navigation bar:

• Click on the logout button.

[[IMAGE: manual_img_358.jpg]]

- A confirm logout dialog box appears.

[[IMAGE: manual_img_359.jpg]]

- Confirm the logout by clicking on the Logout button.

- The user is successfully logged out and redirected to the login page.

[[IMAGE: manual_img_360.jpg]]

From the Profile icon in the top-right corner of the user dashboard:

• Click on the profile icon.

[[IMAGE: manual_img_361.jpg]]

- Choose the Logout option from the profile icon.

[[IMAGE: manual_img_362.jpg]]

- A confirm logout dialog box appears.

[[IMAGE: manual_img_363.jpg]]

- Click on the Logout button.

- The user is successfully logged out and redirected to the login page.

[[IMAGE: manual_img_364.jpg]]

# Summary

The Koili Terminal Management System (TMS) user manual provides comprehensive guidance on effectively utilizing the features within the TMS portal. It covers various modules, including Branch, User, Merchant, IPN, Profile, Settings, Audit Log, and Partner.

Users can seamlessly manage organizational structures, user access, merchant portfolios, IPN devices, and system settings through intuitive interfaces and functionalities. Key features such as API key management, email configuration, and the audit log enhance security and transparency. The Profile module offers personalized spaces for users to access account information, change passwords, and utilize the Notify Checker feature for request review.

Additionally, the Partner module facilitates collaboration with external entities, allowing for independent management of operations through dedicated dashboards. With detailed descriptions and step-by-step instructions provided in this user manual, users can efficiently navigate and utilize the Koili TMS portal to optimize their payment processing workflows and enhance operational efficiency.

Feedback

We welcome your feedback! If you encounter any issues or have suggestions for improvement, please contact us.

Thank You

We appreciate your support and look forward to enhancing the IPN Terminal Management System based on your valuable feedback.

Support

You can contact our technical team regarding any difficulties during the integration process.

Technical Contact

Email: ipn-tech@bitskraft.com

Business Contact Bitskraft Private Limited Naxal, Nagpokhari

Email: info@bitskraft.com Phone: +977-014537311
