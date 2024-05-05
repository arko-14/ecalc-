import math

class DCMotorCalculator:
    def __init__(self):
        self.emf = None
        self.Ia = None

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def calculate_torque(self):
        K = self.get_float_input("Enter the torque constant: ")
        I = self.get_float_input("Enter the armature current: ")
        T = K * I
        print("Torque:", T)
        return T

    def calculate_omega(self):
        V = self.get_float_input("Enter the voltage: ")
        I = self.get_float_input("Enter the armature current: ")
        Ra = self.get_float_input("Enter the armature resistance: ")
        Ke = self.get_float_input("Enter the EMF constant: ")
        
        self.Ia = (V - self.emf) / Ra if self.emf else I
        omega = (V - self.Ia * Ra) / Ke
        print("Omega:", omega)
        return omega

    def calculate_power(self):
        V = self.get_float_input("Enter the voltage: ")
        Ia = self.Ia if self.Ia else self.get_float_input("Enter the armature current: ")
        power = V * Ia
        print("Output power:", power)
        return power

    def calculate_efficiency(self):
        power1 = self.calculate_power()
        power2 = self.calculate_power()
        
        efficiency = (power2 / power1) * 100 if power1 else 0
        print('Efficiency:', efficiency)
        return efficiency

    def calculate_emf(self):
        Ke = self.get_float_input("Enter the EMF constant: ")
        omega = self.calculate_omega()
        self.emf = Ke * omega
        print("EMF:", self.emf)
        return self.emf

    def calculate_armature_current(self):
        V = self.get_float_input("Enter the voltage: ")
        self.emf = self.calculate_emf()
        Ra = self.get_float_input("Enter the armature resistance: ")
        Ia = (V - self.emf) / Ra
        print("Armature Current:", Ia)
        return Ia

    def calculate_armature_resistance(self):
        V = self.get_float_input("Enter the voltage: ")
        Ia = self.calculate_armature_current()
        emf = self.calculate_emf()
        Ra = (V - Ia * emf) / (Ia**2)
        print("Armature Resistance:", Ra)
        return Ra


class BLDCMotorCalculator:
    def __init__(self):
        pass

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def calculate_torque(self):
        K = self.get_float_input("Enter the torque constant: ")
        I = self.get_float_input("Enter the motor current: ")
        T = K * I
        print("Torque:", T)
        return T

    def calculate_omega(self):
        V = self.get_float_input("Enter the voltage: ")
        I = self.get_float_input("Enter the current: ")
        R = self.get_float_input("Enter the phase resistance: ")
        Ke = self.get_float_input("Enter the EMF constant: ")
        
        omega = (V - I * R) / Ke
        print("Omega:", omega)
        return omega

    def calculate_power(self):
        V = self.get_float_input("Enter the voltage: ")
        I = self.get_float_input("Enter the current: ")
        power = V * I
        print("Power:", power)
        return power

    def calculate_efficiency(self):
        power3 = self.calculate_power()
        power4 = self.calculate_power()
        efficiency1 = (power4 / power3) * 100 if power3 else 0
        print('Efficiency:', efficiency1)
        return efficiency1

    def calculate_phase_resistance(self):
        V1 = self.get_float_input("Enter the voltage: ")
        I1 = self.get_float_input("Enter the current: ")
        E = self.get_float_input("Enter the EMF: ")
        R = (V1 - I1 * E) / (I1**2)
        print("Phase Resistance:", R)
        return R

    def calculate_motor_torque(self):
        Kt = self.get_float_input("Enter the torque constant: ")
        I1 = self.get_float_input("Enter the motor current: ")
        Te = Kt * I1
        print("Torque:", Te)
        return Te

    def calculate_mechanical_power(self):
        omega = self.calculate_omega()
        Te = self.calculate_motor_torque()
        mechanical_power = Te * omega
        print("Mechanical Power:", mechanical_power)
        return mechanical_power


class PMMotorCalculator:
    def __init__(self):
        pass

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def calculate_torque(self):
        Kt1 = self.get_float_input("Enter the torque constant: ")
        I = self.get_float_input("Enter the motor current: ")
        Te1 = Kt1 * I
        print("Torque:", Te1)
        return Te1

    def calculate_omega(self):
        V = self.get_float_input("Enter the voltage: ")
        I = self.get_float_input("Enter the current: ")
        R = self.get_float_input("Enter the phase resistance: ")
        Ke = self.get_float_input("Enter the EMF constant: ")
        
        omega = (V - I * R) / Ke
        print("Omega:", omega)
        return omega

    def calculate_power(self):
        V = self.get_float_input("Enter the voltage: ")
        I = self.get_float_input("Enter the current: ")
        power = V * I
        print("Power:", power)
        return power

    def calculate_efficiency(self):
        power5 = self.calculate_power()
        power6 = self.calculate_power()
        efficiency2 = (power6 / power5) * 100 if power5 else 0
        print('Efficiency:', efficiency2)
        return efficiency2

    def calculate_phase_resistance(self):
        V2 = self.get_float_input("Enter the voltage: ")
        I2 = self.get_float_input("Enter the current: ")
        E2 = self.get_float_input("Enter the EMF: ")
        R1 = (V2 - I2 * E2) / (I2**2)
        print("Phase Resistance:", R1)
        return R1

    def calculate_mechanical_power(self):
        Kt = self.get_float_input("Enter the torque constant: ")
        I1 = self.get_float_input("Enter the motor current: ")
        omega = self.calculate_omega()
        Te = Kt * I1
        mechanical_power = Te * omega
        print("Mechanical Power:", mechanical_power)
        return mechanical_power

    def calculate_armature_current(self):
        V = self.get_float_input("Enter the voltage: ")
        E = self.get_float_input("Enter the EMF: ")
        Ra1 = self.get_float_input("Enter the armature resistance: ")
        Ia1 = (V - E) / Ra1
        print("Armature Current:", Ia1)
        return Ia1


class TransformerCalculator:
    def __init__(self):
        pass

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    def calculate_primary_emf(self):
        N1 = self.get_int_input("Enter the number of turns in the primary winding: ")
        phim = self.get_float_input("Enter the magnetic flux contained: ")
        E1 = 4.447 * phim * N1 
        print("EMF induced in primary winding:", E1, "V")
        return E1

    def calculate_secondary_emf(self):
        N2 = self.get_int_input("Enter the number of turns in the secondary winding: ")
        phim = self.get_float_input("Enter the magnetic flux contained: ")
        E2 = 4.447 * phim * N2 
        print("EMF induced in secondary winding:", E2, "V")
        return E2

    def calculate_equivalent_resistance(self):
        r1 = self.get_float_input("Enter the resistance associated with primary winding: ")
        r2 = self.get_float_input("Enter the resistance associated with secondary winding: ")
        N1 = self.get_int_input("Enter the number of turns in the primary winding: ")
        N2 = self.get_int_input("Enter the number of turns in the secondary winding: ")
        r2dash = r2 * (N1 / N2) ** 2 
        re1 = r1 + r2dash
        print("Equivalent resistance:", re1, "ohm")
        return re1

    def calculate_equivalent_reactance(self):
        x1 = self.get_float_input("Enter the reactance associated with primary winding: ")
        x2 = self.get_float_input("Enter the reactance associated with secondary winding: ")
        N1 = self.get_int_input("Enter the number of turns in the primary winding: ")
        N2 = self.get_int_input("Enter the number of turns in the secondary winding: ")
        x2dash = x2 * (N1 / N2) ** 2 
        xe1 = x1 + x2dash
        print("Equivalent reactance:", xe1, "ohm")
        return xe1

    def calculate_secondary_equivalent_resistance(self):
        r1 = self.get_float_input("Enter the resistance associated with primary winding: ")
        N1 = self.get_int_input("Enter the number of turns in the primary winding: ")
        N2 = self.get_int_input("Enter the number of turns in the secondary winding: ")
        r1dash = r1 * (N2 / N1) ** 2
        r2 = self.get_float_input("Enter the resistance associated with secondary winding: ")
        re2 = r2 + r1dash
        print("Secondary equivalent resistance:", re2, "ohm")
        return re2

    def calculate_secondary_equivalent_reactance(self):
        x1 = self.get_float_input("Enter the reactance associated with primary winding: ")
        N1 = self.get_int_input("Enter the number of turns in the primary winding: ")
        N2 = self.get_int_input("Enter the number of turns in the secondary winding: ")
        x1dash = x1 * (N2 / N1) ** 2
        x2 = self.get_float_input("Enter the reactance associated with secondary winding: ")
        xe2 = x2 + x1dash
        print("Equivalent reactance:", xe2, "ohm")
        return xe2

    def calculate_efficiency(self):
        Idash = self.get_float_input("Enter the current consumed: ")
        Res = self.get_float_input("Enter the resistance: ")
        wcu = Idash ** 2 * Res
        x = self.get_float_input("Enter the amount of load: ")
        xdash = self.get_float_input("Enter the value of x: ")
        cosine = math.cos(xdash)
        print("The cosine value of xdash is:", cosine)
        kVa = self.get_float_input("Enter the value of kVa: ")
        W1 = self.get_float_input("Enter the iron loss: ")
        efficiency3 = ((x * kVa * cosine) / (x * kVa * cosine + (W1 + x ** 2 * wcu))) * 100 
        print("Efficiency:", efficiency3, "%")
        return efficiency3

# Instantiate the classes and call the methods
while True:
    print("Choose an option:")
    print("1. DC Motor")
    print("2. BLDC Motor")
    print("3. PMDC Motor")
    print("4. Transformer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        motor_calculator = DCMotorCalculator()
        while True:
            print("1. Calculate Torque")
            print("2. Calculate Omega")
            print("3. Calculate Power")
            print("4. Calculate Efficiency")
            print("5. Calculate EMF")
            print("6. Calculate Armature Current")
            print("7. Calculate Armature Resistance")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                motor_calculator.calculate_torque()
            elif choice == '2':
                motor_calculator.calculate_omega()
            elif choice == '3':
                motor_calculator.calculate_power()
            elif choice == '4':
                motor_calculator.calculate_efficiency()
            elif choice == '5':
                motor_calculator.calculate_emf()
            elif choice == '6':
                motor_calculator.calculate_armature_current()
            elif choice == '7':
                motor_calculator.calculate_armature_resistance()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
    elif choice == '2':
        motor_calculator = BLDCMotorCalculator()
        while True:
            print("1. Calculate Torque")
            print("2. Calculate Omega")
            print("3. Calculate Power")
            print("4. Calculate Efficiency")
            print("5. Calculate Phase Resistance")
            print("6. Calculate Mechanical Power")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                motor_calculator.calculate_torque()
            elif choice == '2':
                motor_calculator.calculate_omega()
            elif choice == '3':
                motor_calculator.calculate_power()
            elif choice == '4':
                motor_calculator.calculate_efficiency()
            elif choice == '5':
                motor_calculator.calculate_phase_resistance()
            elif choice == '6':
                motor_calculator.calculate_mechanical_power()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
                
    elif choice == '3':
        motor_calculator = PMMotorCalculator()
        while True:
            print("1. Calculate Torque")
            print("2. Calculate Omega")
            print("3. Calculate Power")
            print("4. Calculate Efficiency")
            print("5. Calculate Phase Resistance")
            print("6. Calculate Mechanical Power")
            print("7. Calculate Armature Current")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                motor_calculator.calculate_torque()
            elif choice == '2':
                motor_calculator.calculate_omega()
            elif choice == '3':
                motor_calculator.calculate_power()
            elif choice == '4':
                motor_calculator.calculate_efficiency()
            elif choice == '5':
                motor_calculator.calculate_phase_resistance()
            elif choice == '6':
                motor_calculator.calculate_mechanical_power()
            elif choice == '7':
                motor_calculator.calculate_armature_current()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

    elif choice == '4':
        transformer_calculator = TransformerCalculator()
        while True:
            print("1. Calculate Primary EMF")
            print("2. Calculate Secondary EMF")
            print("3. Calculate Equivalent Resistance")
            print("4. Calculate Equivalent Reactance")
            print("5. Calculate Secondary Equivalent Resistance")
            print("6. Calculate Secondary Equivalent Reactance")
            print("7. Calculate Efficiency")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                transformer_calculator.calculate_primary_emf()
            elif choice == '2':
                transformer_calculator.calculate_secondary_emf()
            elif choice == '3':
                transformer_calculator.calculate_equivalent_resistance()
            elif choice == '4':
                transformer_calculator.calculate_equivalent_reactance()
            elif choice == '5':
                transformer_calculator.calculate_secondary_equivalent_resistance()
            elif choice == '6':
                transformer_calculator.calculate_secondary_equivalent_reactance()
            elif choice == '7':
                transformer_calculator.calculate_efficiency()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
