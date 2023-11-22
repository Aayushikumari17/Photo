# Photo
 Future Ready Talent - Project Documentation

Name – Aayushi Kumari

<h1>Project Title – Cloud Photo Storage</h1>

<h2>Project Statement</h2>

<h2>Project Aim</h2>

The primary aim of this project is to develop an Azure-based Image Upload and Display Application that empowers users to effortlessly upload images and access them alongside essential information. This application leverages Azure Virtual Machine to ensure a seamless, scalable, and reliable experience. Users can upload images in various formats and enhance them with titles, descriptions, and tags for improved organization and search ability.

The application fosters a user-friendly environment, offering image browsing, searching, and filtering features. By incorporating Azure services for data storage and authentication, it ensures data security and privacy. Furthermore, the project embraces responsive design for compatibility across devices and incorporates analytics for performance monitoring.

This platform caters to a wide range of users, from individuals managing personal photo collections to businesses seeking to establish a community-driven image repository. Ultimately, the Azure-based Image Upload and Display Application aims to provide an efficient and accessible solution for image management and sharing.




<h2>Description</h2> 

 	The application allows users to upload images and then displays the uploaded images with some basic information. You can deploy this project on Azure App Service. 
Overview:
The Azure-based Image Upload and Display Application is a web-based platform designed to allow users to easily upload images and view them alongside basic information. It leverages the capabilities of Azure App Service to ensure scalability, reliability, and a seamless user experience.

<h2>Key Features:</h2>

<h2>1.	Image Upload:</h2>

     Users can easily upload their images through a user-friendly interface. The                    application supports a variety of image formats, such as JPEG, PNG, and GIF.

<h2>2.	Image Information:</h2>

     After uploading an image, users can provide basic information about it, such as a title, description, and tags. This information enhances the searchability and organization of the uploaded images.

<h2>3.	Image Display:</h2>

Uploaded images and their associated information are displayed in a visually appealing and organized manner. Users can browse through the collection of images and view details by clicking on individual images.

<h2>4.	Search and Filter:</h2>

The application offers a search and filter functionality, enabling users to find specific images based on titles, descriptions, or tags. This feature enhances user experience and helps them quickly locate the content they're interested in.

<h2>5.	User Authentication:</h2>

To ensure data security and user privacy, the application can implement user authentication and authorization using Azure Active Directory or other identity providers.

<h2>6.	Scalability:</h2>

Leveraging Azure App Service, the application can seamlessly handle increased traffic and demand. It can be auto-scaled to accommodate varying numbers of users and concurrent uploads.

<h2>7.	Data Storage:</h2>

Uploaded images and their associated information are securely stored in Azure Blob Storage or a similar data repository. This ensures reliable and durable storage for the uploaded content.

The application is designed to be responsive, ensuring it works seamlessly on various devices, including desktops, tablets, and smartphones.
Analytics and Monitoring:

Utilize Azure Application Insights to monitor the application's performance, track usage, and identify potential issues for quick resolution.
Deployment:
The Image Upload and Display Application can be deployed on Azure App Service, which offers a fully managed platform for building, deploying, and scaling web apps. The deployment process includes configuring the web app, setting up the database or data storage, and enabling any necessary security measures and scaling options.

This project is ideal for individuals or businesses looking to create a user-friendly and scalable image-sharing platform. Whether it's for personal photo collections or a community-driven image repository, the Azure-based Image Upload and Display Application offers a robust and reliable solution.




Azure Services Used –
Virtual Machine 
Azure SQL Database
Azure Storage account

Other Services Used – 
Bash Scripts
Network security group

Environment Used-
VM – Linux (ubuntu 20.04)
System – Windows 11


<h2>Project Walkthrough</h2>

o	Create an Azure free account, sign into my Azure Portal<br>
o	Click on virtual machine tab, create virtual machine 

![vm1](https://github.com/SapnaBurute/final-Project/assets/134684026/420fd52a-36f9-4672-a28b-0bb3bced0e98)
 

o Subscription- Free Trial
o Resource group- photos-vm
o Virtual machine name- new-vm
o Region- West US 3 (Zone 1)

 o Leave disks tab as default
 ![vm2](https://github.com/SapnaBurute/final-Project/assets/134684026/53a67040-f093-4d6d-9343-a0df74e271a6)
 
<h2>Connect to virtual machines</h2>


There are several ways to access your Azure virtual machines. The Azure portal supports options for connecting your Windows and Linux machines, and making connections by using Azure Bastion. The following diagram shows how you can connect Azure virtual machines with the SSH and RDP protocols, Cloud Shell, and Azure Bastion.
 ![vm3](https://github.com/SapnaBurute/final-Project/assets/134684026/05549dc7-5527-45a1-8dc4-bd18583b194f)
Architecture diagram

<h2>NOW CREATE A STORAGE ACCOUNT</h2>

o Subscription- Free Trial
o Resource group- photos-vm
o Storage account Name- photosto11
o Region- central(india)

![storage Account](https://github.com/SapnaBurute/final-Project/assets/134684026/a867bb3e-7f8a-420a-ac62-0ad73baaea27)

I have created Storage accounts  to store and manage photo in cloud environments, typically in the context of cloud computing platforms like Microsoft Azure,. They serve several important purposes:

Data Storage: Storage accounts provide a secure and scalable place to store various types of data, such as files, blobs, tables, queues, and virtual machine disks.

Scalability: They can scale to accommodate growing amounts of data, making them suitable for a wide range of applications, from small projects to large enterprises.

Data Redundancy: Storage accounts often offer features like data replication and redundancy to ensure data durability and availability. This means your data is stored in multiple locations, reducing the risk of data loss.

Accessibility: They allow you to access and manage your data over the internet or within a cloud network, making it accessible from anywhere.

Integration: Storage accounts can be integrated with various cloud services and applications, enabling you to build and deploy solutions that require data storage, retrieval, and processing.

Security: They offer security features, such as access control, encryption, and authentication, to protect your data from unauthorized access and breaches.

Cost Management: Cloud providers typically offer different storage tiers with varying costs, so you can choose the most cost-effective option for your specific use case.

In summary, storage accounts are a fundamental component in cloud computing, offering reliable and scalable data storage solutions for a wide range of applications and services.



<h2>CONNECT STORAGE ACCOUNT TO WEBSITE</h2>

•	First go to access key of storage account
•	Copy the connection string of storage account and paste into code 

![Access Key](https://github.com/SapnaBurute/final-Project/assets/134684026/2d8cab00-2be8-4e98-ae9b-7ed64bf64edc)

 


•	I have created storage account to store photos which any user will upload in my website


•	Storage accounts are used for a variety of purposes in the context of cloud computing, particularly in platforms like Microsoft Azure. Here are some common reasons why storage accounts are used:

•	Data Storage: Storage accounts are primarily used to store data, including files, documents, images, videos, and more. They provide scalable and reliable storage options for both structured and unstructured data.

•	Backup and Recovery: Storage accounts can be used to create backups of your data, ensuring data resilience and enabling recovery in case of data loss or disasters.

<h2>CREATE A  AZURE SQL DATABASE SERVER</h2> 


•	Resource group (move):  photos-vm
•	Status: Online
•	Location: Central India
•	Subscription (move): Free Trial
•	Subscription ID: 4f7f032d-b4af-41de-9967-bf51447c8cd0
•	Server name: photo.database.windows.net
•	Connection strings: Show database connection strings

![sql db](https://github.com/SapnaBurute/final-Project/assets/134684026/83be5299-8860-4c3d-a155-f9ab2cc5a0ad)

<h2>CONNECT AZURE SQL DATABASE TO WEBSITE</h2>

![sql db](https://github.com/SapnaBurute/final-Project/assets/134684026/83be5299-8860-4c3d-a155-f9ab2cc5a0ad) <br>
•	First go to connection string
•	Then paste the connection string in your code
![vm cli](https://github.com/SapnaBurute/final-Project/assets/134684026/d869bb71-d178-4522-8c69-5f30686d27d0) <br>

<h2>NOW CONNECT THE VM SSH USING AZURE CLI</h2>

![sudo apt](https://github.com/SapnaBurute/final-Project/assets/134684026/c794ae67-e100-407f-8af4-b4c34a9dd795) <br>

<h2>NOW IN TERMINAL WRITE THE COMMAND</h2>
1.	sudo apt update && sudo apt upgrade –y
2.	sudo apt install python3 python3-pip git -y
3.	sudo apt install msodbcsql17
4.	mkdir app
5.	cd app

![vm inbound](https://github.com/SapnaBurute/final-Project/assets/134684026/ea451b90-6a1e-416f-9e11-24f021e40459)<br>

<h2>OPEN THE INBOUND PORT OF VM</h2>

![vm connect](https://github.com/SapnaBurute/final-Project/assets/134684026/6f06d22d-807d-4faf-9e2f-48a96fd85370)<br>

<h2>GIT CLONE</h2>

![vm connect](https://github.com/SapnaBurute/final-Project/assets/134684026/6f06d22d-807d-4faf-9e2f-48a96fd85370)<br>

<h2>Now the run the command python3 aap.py</h2>
![vm connect p3](https://github.com/SapnaBurute/final-Project/assets/134684026/194416ea-00cb-437d-9945-1a195a2487e8)<br>
Project Conclusion-

<h2>OUTPUT</h2>

![log in](https://github.com/Aayushikumari17/Photo/assets/115334350/af540e18-f162-4fc1-8216-8962a14bceaa)<br>

<h2>SIGN UP</h2>

![sign up](https://github.com/SapnaBurute/final-Project/assets/134684026/a64c8e72-d886-45bf-8305-f44731b05388)<br>

<h2>LOGIN PAGE</h2>

![uplod img](https://github.com/SapnaBurute/final-Project/assets/134684026/0612efbc-193d-4d5e-af7c-b306ce96155a)<br>


<h2>PHOTO GALLERY</h2>

![uplod img](https://github.com/SapnaBurute/final-Project/assets/134684026/0612efbc-193d-4d5e-af7c-b306ce96155a)<br>

<h2>CONCLUSION</h2>
In conclusion, the Azure-based Image Upload and Display Application represents a dynamic and versatile solution for users seeking a seamless and efficient way to manage and share images. By harnessing the power of Azure App Service and various Azure features, this project provides a robust platform that facilitates image uploading, organization, and accessibility.

Users can easily upload their images, enrich them with essential information, and navigate their collection with ease. The application's search and filter functionality enhances user experience, while responsive design ensures accessibility across different devices.

With a strong focus on data security and privacy, the project offers peace of mind to both individuals and businesses. Additionally, the scalability of the application allows it to adapt to fluctuating demands, making it an ideal choice for diverse user bases.

This project underscores the power of cloud-based services and modern web application development, delivering a reliable, user-friendly, and feature-rich environment for image management. Whether for personal or professional use, the Azure-based Image Upload and Display Application stands as a valuable and efficient tool for sharing and managing images.








For documentation click on the link https://docs.google.com/document/d/1rmz0BgdBoVjhgLc5MjrZ_7QPSE8A7aa0/edit?usp=sharing&ouid=102905264427811203114&rtpof=true&sd=true <br> <br>
for demo video click on this link https://drive.google.com/file/d/16Zur2XTQLnws16Und8xJR--qqM7nwD8v/view?usp=drivesdk <br> <br>
project demo url click on this click http://98.70.42.132:3000 
