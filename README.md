# How to make a preseeded Debian ISO

1. **Download isomaster**

    ```
    sudo apt-get install isomaster
    ```

1. **Create a simple preseed file**

    We can do it by running the simple_seed_creator.py script:
    ```
    python simple_seed_creator.py
    ```

1. **Edit the preseed.seed**
    Change username, hostname, network configuration, etc.
    
    By default root password is toor.
    
    For safety reasons it's recommended that you change the passwords **after** the install and do not write definitive passwords in the preseed.seed file.

1. **Insert files in debian ISO**
    
    Open isomaster and load the desired iso to be converted to a preseeded one.
    
    Now put the recently created preseed.seed file into the / of the ISO (don't worry, doing this does not modifies the original ISO).
    
    And then, put the files isolinux/install.cfg and isolinux/isolinux.cfg into the isolinux directory inside the ISO.
    
    Now save the ISO (File -> Save as)


Note:
I must test using the preseed in an USB. Should the path to the preseed.seed be changed to /hd-media/preseed.seed?
