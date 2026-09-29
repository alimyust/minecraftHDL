import os
import parser
import subprocess



def run_yosys_script():
    result = subprocess.run(["yosys", "build.ys"], check=True)

    if result.returncode == 0:
        print("Yosys build successful!")
    else:
        print("Yosys build failed.")

def run_parser():
    pass
    parser()
    


def main():
    run_yosys_script()   
    run_parser()

if __name__=="__main__":
    main()
