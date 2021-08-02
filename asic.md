# ASIC Design

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