# Assembler - Forensics, 100 баллов
```bash
$ file assembler
assembler: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped
```
Как видим, это исполняемый файл для Linux. Давайте посмотрим, какие системные вызовы совершает эта программа при работе.
```bash
$ strace ./assembler
execve("./assembler", ["./assembler"], [/* 18 vars */]) = 0
creat("/tmp/flag", 0755)                = 3
write(3, "y", 1)                        = 1
write(3, "t", 1)                        = 1
write(3, "c", 1)                        = 1
write(3, "t", 1)                        = 1
write(3, "f", 1)                        = 1
write(3, "{", 1)                        = 1
write(3, "a", 1)                        = 1
write(3, "s", 1)                        = 1
write(3, "s", 1)                        = 1
write(3, "3", 1)                        = 1
write(3, "m", 1)                        = 1
write(3, "b", 1)                        = 1
write(3, "l", 1)                        = 1
write(3, "3", 1)                        = 1
write(3, "r", 1)                        = 1
write(3, "}", 1)                        = 1
exit(0)                                 = ?
+++ exited with 0 +++
```
Как видим, программа создала файл `/tmp/flag`. Посмотрим его и получим флаг. 

**Флаг:** `ytctf{ass3mbl3r}`
