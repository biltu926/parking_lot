1. Instructions to run the project
    1. The scripts directory contains a python script parking_lot_script.py, which runs the sample
        input files present in the same directory [example1.txt, example2.txt, example3.txt].
    2. At a time only one exampele file is being read and run. So, kindly change the name, i.e, 
        example2.txt, example3.txt etc to run the input files.
    3. The output gets saved in a file called output.txt in the same directory (/scripts).
        The file gets appended with the output.
    4. To run the script kindly execute the following command from directory parking_lot.
        python -m scripts.parking_lot_script

2. Instructions to run the testcases.
    1. To run the testcases run the following command from inside parking_lot.
        python -m unittest discover
    2. The testcases cover the cases where vehicles are parked for varying time period, and checks
        the fees accordingly.