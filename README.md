# Project Title
GmE 205 - Laboratory Exercise 4

# How to set up the virtual environment
1. Create a folder on your computer and open it in your IDE (e.g., VS Code)
2. Open the terminal then create the virtual environment by running the following:
    ```
    py -m venv .venv
    .\.venv\Scripts\activate
    ```
3. Press ```Ctrl + Shift + P``` in VS Code, search for *Python: Select Interpreter*, then choose the interpreter inside the ```.venv``` folder
4. Install the required packages by running the following in the terminal:
    ```
    python -m pip install --upgrade pip
    pip install pandas matplotlib
    ```
5. (Recommended) List the installed packages via:
    ```
    pip freeze > requirements.txt
    ```

# How to run Python scripts

In the terminal, ensuring that ```(.venv)``` is present in the prompt, run the following:
    ```
    python <folder/script_name.py>
    ```

# Reflections
- Polymorphism appears in the methods shared but modified by the different feature types. The most obvious example is `effective_area()`, which the 3 feature classes overrode from the base SpatialObject class). However, the methods `from_dict()` and `as_dict()` also effectively show polymorphism (in the form of duck typing), where the Parcel, Building, and Road classes share similarly-named methods that they did not inherit from any base class.
- With polymorphism, end users can use similarly-named methods (with similar expected inputs and outputs) while allowing these methods to have different inner workings. This allows the user to not have to use conditional logic to select which specific method to apply based on type. Instead, the user can simply use the similarly-named method while delegating the specific methodology to the class.
- Both inheritance and polymorphism allow multiple spatial classes to share methods. However, while inheritance allows classes to share the method itself, polymorphism allows the sharing of method names while specializing their inner workings.
- It is better for objects to compute their own area because it makes sense that their own specialized logic for area calculation is assigned to them. This takes the responsibility off of the main program execution flow to have to decide which specific area calculation logic to use, limiting the potential for bugs and errors and making future debugging and refactoring easier.
- To add a new class in the program, it would simply have to be defined in `spatial.py`: its attributes and methods, including the shared method of `effective_area()`. This is the strength of OOP in general, and polymorphism in general: it is easy to scale in terms of more classes.