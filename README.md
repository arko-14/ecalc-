# ecalc-


Sure, here's a description of the project logic:

Project Logic Description
The Motor and Transformer Calculator project is designed to provide a versatile tool for engineers and enthusiasts to perform calculations related to various types of electric motors (DC, BLDC, PMDC) and transformers. The project is implemented in Python and consists of a command-line interface (CLI) that guides users through the process of selecting a motor type and performing specific calculations.

Key Components:
Main Loop: The project starts with a main loop where users are prompted to choose between different motor types (DC, BLDC, PMDC) or a transformer calculator. This loop ensures that users can select the desired functionality easily.
Motor Classes: Each motor type (DC, BLDC, PMDC) is represented by a separate Python class (DCMotorCalculator, BLDCMotorCalculator, PMMotorCalculator) containing methods to perform specific calculations such as torque, speed, power, efficiency, EMF, armature current, and armature resistance. These classes encapsulate the functionality related to each motor type, making the code modular and easy to maintain.
Transformer Class: The TransformerCalculator class handles calculations related to transformers, including primary and secondary EMF, equivalent resistance, equivalent reactance, and efficiency. Similar to the motor classes, the Transformer class provides methods to perform specific calculations for transformers.
Input Validation: Throughout the project, input validation is implemented to ensure that users enter valid numerical values. Error handling is included to handle cases where invalid input is provided, prompting users to re-enter the correct information.
User Interaction: The CLI interface guides users through the calculation process by presenting a series of prompts and options. Users can select the desired calculation (e.g., torque, power, efficiency) and enter the required input values when prompted.
Reusable Code: The project emphasizes code reusability by encapsulating functionality into separate classes and methods. This approach allows for easy extension and modification of the project, as each component can be independently tested and updated without affecting other parts of the codebase.
Usage:
