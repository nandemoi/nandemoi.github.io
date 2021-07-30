# 2021q3 Homework1 (quiz3)

contributed by nandemoi

## quiz3-2  

只有完成這半題

```C
static int unhide_process(pid_t pid)
{
    pid_node_t *proc, *tmp_proc;
    list_for_each_entry_safe (proc, tmp_proc, &hidden_proc, list_node) {
        if (proc->id == pid) { // Todo: hash srch
            list_del(&proc->list_node);
            kfree(proc);
        }
    }
    return SUCCESS;
}

#define HW1 1

#if HW1
static void multipid (char *message, int (*proc)(pid_t)) {
    long pid;
    char delims[] = " \t";
    char pid_str_buf [8]; // Todo: cat /proc/sys/kernel/pid_max
    char *nxt_tok = message, *nxt_tok0;
    pr_info ("start\n");
    for (strsep (&nxt_tok, delims); nxt_tok; ) { // Todo:  test add/del nothing
        nxt_tok0 = nxt_tok;
        strsep (&nxt_tok, delims);
        if (nxt_tok) {
            memcpy (pid_str_buf, nxt_tok0, nxt_tok - nxt_tok0);
            pid_str_buf [nxt_tok - nxt_tok0] = '\0';
            printk ("hideproc to do proc %s\n", pid_str_buf);
            kstrtol(pid_str_buf, 10, &pid);
        } else { // should fail w/o ad hoc (1)
            printk ("hideproc last to do proc %s\n", nxt_tok0);
            kstrtol(nxt_tok0, 10, &pid); 
        }
        (*proc)(pid);
    }
}
#endif

static ssize_t device_write(struct file *filep,
                            const char *buffer,
                            size_t len,
                            loff_t *offset)
{
    char *message;

    char add_message[] = "add", del_message[] = "del";
    if (len < sizeof(add_message) - 1 && len < sizeof(del_message) - 1)
        return -EAGAIN;

    message = kmalloc(len + 2, GFP_KERNEL); // Todo: add hoc, was +1 ...(1)
    memset(message, 0, len + 2); // Todo: add hoc, was +1 ...(1)
    copy_from_user(message, buffer, len);
    if (!memcmp(message, add_message, sizeof(add_message) - 1)) {
#if HW1
        multipid (message, hide_process);
#else
        kstrtol(message + sizeof(add_message), 10, &pid);
        hide_process(pid);
#endif
    } else if (!memcmp(message, del_message, sizeof(del_message) - 1)) {
#if HW1
        multipid (message, unhide_process);
#else
        kstrtol(message + sizeof(del_message), 10, &pid);
        unhide_process(pid);
#endif
    } else {
        kfree(message);
        return -EAGAIN;
    }

    *offset = len;
    kfree(message);
    return len;
}
```

## quiz1

1. ```_hideproc_init()``` calls ```init_hook()``` where  
    1. ```find_ge_pid``` looked up with ```kallsyms_lookup_name()``` and both assigned to ```real_find_ge_pid``` and stored in ```hook.org```

2. ```ps``` queries ```procfs``` (```/proc```).  

## quiz4

1. ```hook_find_ge_pid()``` to employ hash search instead?

2. ```init_hook()``` uses ```kallsyms_lookup_name()``` to look up ```find_ge_pid``` and afterward in ```hook_install()``` calls ```hook_resolve_addr()``` where the same thing is performed again except via the ```hook``` fields. ```hook_install()```/```hook_resolve_addr()``` seems to be called only once at the installation/beginning of hideproc so this may be simplified? 

## [題目連結](https://hackmd.io/@sysprog/linux2021-summer-quiz1)  

## Journal: 

1. ```multipass mount```  
2. multipass VM 如果 hang 住就 ```stop``` 再 ```start``` 就好了  
3. 不熟的 functions 老老實實寫個小程式測試好確定功能後再用。  

在設定一個適合的開發環境花了很多時間：

1. Ubuntu Virtual Machine 和 Raspbian 都有 EFI 的問題。Raspbian 從 source make 完成後沒有繼續試，先用 multipass。

2. Kernel module development 大概沒有辦法掛 ```gdb``` 做 single-stepping debug，只能用 inline message logging 的 batch flow 來 debug。再加上 memory manipulation、pointers 的使用要很 meticulous，一些 function 的 kernel counter parts 的用法或者不太一樣，或者不熟、我的記憶 got rusty，一出錯 system 就 hang 或者其後的 operations 無法執行或者一樣 hang 住。

3. 不想用 ```vi``` 或 ```nano```，一開始還不知道可以用 ```multipass mount``` 而用 ```sshfs```，讓 MacOS 也受到影響，整個拖慢常常要重開機；就想說用 Ubuntu VM 跑 multipass，這樣如果要重開機重開虛擬機就好。結果發現 nested virtualization 不支援。
   
[Can I use strtok() in a Linux Kernel Module?](https://stackoverflow.com/questions/2246618/can-i-use-strtok-in-a-linux-kernel-module)  



###### tags: `Linux 2021`  
