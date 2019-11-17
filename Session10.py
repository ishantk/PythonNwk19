cisco = {
    "device_type": "cisco_ios",
    "host": "cisco.domain.com",
    "username": "admin",
    "password": "cisco123"
}

"""
    DATABASE : RDBMS Model -> MySQL
        Collection of Tables
        Collection of Rows & Columns
        
        Devices
        -------
        
        ---------------------------------------------------------
        id  deviceType  host                username    password
        ---------------------------------------------------------
        1   cisco_ios   cisco.domain.com    admin       cisco123
        2   cisco_ios   cisco.domain.com    admin       cisco123
        
        SQL : Structured Query Language
              
              > Create Tables
              ---------------
              create table Devices(
                id int primary key auto_increment,
                deviceType varchar(256),
                host varchar(256),
                username varchar(256),
                password varchar(256)
              )
              
              > Insert Data into Tables
              -------------------------
              insert into Devices values (null, 'cisco_ios', 'cisco.domain.com', 'admin', 'cisco123')
              
              > Update Data in Tables
              -----------------------
              update Devices set password = 'pass123' where id = 1
              update Devices set username='john', password = 'john123' where id = 2
              
              
              > Delete from Table
              -------------------
              delete from Devices where id = 1
              
              
              > Fetch Data from Table
              -----------------------
              select * from Devices
              select deviceType, username from Devices
              select deviceType, username from Devices where id = 2
              select deviceType, username from Devices where id > 1 
              
              Explore More of SQL Commands Here : https://www.w3schools.com/sql/
              
        Step1: > Lets perform all the above operations in MySQL DB
        Step2: > Lets perform all the above operations using python in MySQL DB      
        
"""