## LAB3 - Python Ansible
---

Ansible is known for its simplicity and agentless automation tool used for configuration management and application deployment. Ansible is written in Python, which make it easy to

* Execute Python scripts
* Writing custom Ansible modules

In this lab, we will show you how to run a Python script on a remote host using Ansible and write a Ansible module.

### Exercise 1 - Running a Python script on a remote host using Ansible

In this exercise, we will use the Ansible script module to copy the *uname.py* script to the remote host and execute it. Here is the *uname.py* in the *scripts/* directory. Here is the Ansible playbook, *run-python.yml*, to run the script.


```
---
- hosts: all

  tasks:
    - name: execute the uname.py script on a remote host
      script: scripts/uname.py
      register: script_output

    - debug:
        var: script_output
```

From you Jupytehub web Terminal, run the following commands:

```console
$ cd ~/bootcamp/python
$ cat scripts/uname.py
$ ansible-playbook -i runner<n>.lab.mpt.local, -u ubuntu --private-key=~/.ssh/id_rsa_ubuntu run-python.yml
```

You should see the debug output likes like below.

```
TASK [debug] ***********************************************************************************************************************
ok: [ops01] => {
    "script_output": {
        "changed": true,
        "failed": false,
        "rc": 0,
        "stderr": "Shared connection to ops01 closed.\r\n",
        "stderr_lines": [
            "Shared connection to ops01 closed."
        ],
        "stdout": "Linux ops01 4.4.0-166-generic #195-Ubuntu SMP Tue Oct 1 09:35:25 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux\r\n",
        "stdout_lines": [
            "Linux ops01 4.4.0-166-generic #195-Ubuntu SMP Tue Oct 1 09:35:25 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux"
        ]
    }
}
```


### Exercise 2 - Creating a custom module

Ansible provides lots of modules to perform various tasks for many well known devices. If you have a legacy device that is not supported by Ansible, you can write you own Ansible module using the following Ansible module template.

Let's start by creating the following file structure in the ~/bootcamp/python home directory.

```
custom-module.yml
library/
└── my_router.py

```

1. From you console Terminal window, create the file structure above.

```console
$ cd ~/bootcamp/python
$ touch custom-module.yml
$ mkdir -p library
$ touch library/my_router.py
```

2. Next edit the *library/my_router.py* file and add the following lines of code.

```
#! /usr/bin/env python3

from ansible.module_utils.basic import *

def main():
	module = AnsibleModule(argument_spec={})
	response = {"My": "Router"}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
```

3. From the Terminal window, open the *custom-module.yml* playbook to add the following lines of code:

```
---
- hosts: all

  tasks:
    - name: test my_router module
      my_router: 
      register: result

    - debug: var=result  

```

4. Now we have created the custom module and the ansible playbook. Let's test it by running the following shell command.

```console
$ cd ~/bootcamp/python
$ ansible-playbook -i runner<n>.lab.mpt.local, -u ubuntu --private-key=~/.ssh/id_rsa_ubuntu custom-module.yml
```

You should see the console output looks like below:


```
PLAY [all] *************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************
ok: [ops01]

TASK [test my_router module] *******************************************************************************************************
ok: [ops01]

TASK [debug] ***********************************************************************************************************************
ok: [ops01] => {
    "result": {
        "changed": false,
        "failed": false,
        "meta": {
            "My": "Router"
        }
    }
}

PLAY RECAP *************************************************************************************************************************
ops01                      : ok=3    changed=0    unreachable=0    failed=0
```

### Conclusion

In this lab, we brief introduce how to use Ansile playbook to run a Python script. Also we created a very simple custom Ansible module. You can use this a starting template to write more advance modules. You can read more about how to write Ansible module using this documentation.

https://docs.ansible.com/ansible/2.8/dev_guide/developing_modules_general.html



