# Chrome_Dinosaur_Game

Well-known Chrome Dinosaur game.

### To run this script you need to:
  - Install python interpreter version 3.10+ from:
    * https://www.python.org/;
  - Create virtual environment with **cli command**:
    * **python3 -m venv venv**;
  - Activate the virtual environment with:
    * **source venv/bin/activate**;
  - Install all dependencies to your virtual environment from 'requirements.txt' with:
    * **pip install -r requirements.txt**;
    
### Set up parameters:
  - Open **main.py** file and scroll it down to "**if __name__ == '__main__':**" statement:
    * Set **script_mode** to **True** if you want to run it in **Training mode**
    * Set **script_mode** to **False** if you want to run it in **Run model mode**
    * Set **save_every_n_generations** if you want to save checkpoints (works in **Training mode** only)
    * Set **restore_from_generation** (0 by default) to run from saved checkpoint (works in **Training mode** only)
    
  - Run the csript;
  
  - Enjoy :)
