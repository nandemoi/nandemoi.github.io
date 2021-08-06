# ASIC Design

## [COSCUP](https://moptt.tw/p/Tech_Job.M.1627103659.A.B1D)

### [HDLS](https://www.eettaiwan.com/20170925ta31-digital-hardware-design/)  

  * Descriptive: sequential vs. parallelism
  * clocking  

#### [Chisel](https://mybinder.org/v2/gh/freechipsproject/chisel-bootcamp/master)

- [Jupyter Scala Kernel](https://almond.sh/docs/quick-start-install)  
  ```cs launch --fork almond:0.10.0 --scala 2.12.11 -- --install```  
  ```jupyter kernelspec list```  
- download source/* (yet to find out how to download a Binder folder in batch instead by hands)  

### [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane)  

### [nMigen](https://github.com/m-labs/nmigen)  

### Formal Verification

#### [SymbiYosys](http://www.clifford.at/papers/2017/smtbmc-sby/)  

#### [EBMC](http://www.cprover.org/ebmc/)  

### FPGA, courses with Quartus, Wifiboy

* [FPGA系統設計實務](https://univ.deltamoocx.net/courses/course-v1:AT+AT_027_1092+2021_02_22/about)  
* [Xylinx PyNQ-Z2](https://youtu.be/RGqStx-Ml7U)

## Synthesis

* [UTexas](http://users.ece.utexas.edu/~adnan/syn-07/)  
* [Berkeley](https://people.eecs.berkeley.edu/~brayton/courses/219b/219b.html)  

## Verilog Simulation

### [Race Condition](http://www.testbench.in/TB_16_RACE_CONDITION.html)  

[Achieving Determinism in SystemVerilog 3.1 Scheduling
Semantics](https://www.accellera.org/images/eda/sv-bc/att-0529/01-sv31schedsemantics-dvcon03.pdf)  

* §3 non-blocking assignments  

    ```verilog
    always @(posedge clk) begin
        c = b;
        b = a;
    end
    ```

    =>

    ```verilog
    always @(posedge clk) c <= b;
    always @(posedge clk) b <= a;
    ```

    [標題[心得] Verilog使用nonblocking assignment解決race問題](https://www.ptt.cc/bbs/Electronics/M.1282650262.A.4AB.html)  

* §4  

    ```verilog
    assign #0 gclk = clk;
    always @(posedge gclk) b = a;
    always @(posedge clk) c = b;
    ```

    According to the IEEE Verilog standard this coding is
    guaranteed to simulate correctly and is also code that
    synthesizes correctly.

### Multithreaded Simulation

* [A Horrible Idea Multithreaded Verilog Simulator / Icarus Verilog](https://iverilog.fandom.com/wiki/A_Horrible_Idea_Multithreaded_Verilog_Simulator)  
* [Verilator 4.0: Open Simulation Goes Multithreaded](https://www.veripool.org/papers/Verilator_v4_Multithreaded_OrConf2018.pdf)  
* [Parallel Multi-core Verilog HDL Simulation](https://scholarworks.umass.edu/cgi/viewcontent.cgi?article=1029&context=dissertations_2)  
* [Parallel Multi-core Verilog HDL Simulation Using Domain Partitioning](https://www.researchgate.net/publication/283654225_Parallel_Multi-core_Verilog_HDL_Simulation_Using_Domain_Partitioning)  