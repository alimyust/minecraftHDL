module test_adder (
    input [1:0] a,
    input [1:0] b,
    output [2:0] sum
);
    // Yosys will break this high-level addition down into gates
    assign sum = a + b;
endmodule