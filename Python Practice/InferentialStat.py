import numpy as np 
from scipy.stats import norm, t, linregress
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class infer_Stats():
    def __init__(self):
        self.arr = None
        pass

    def z_Test(self, Ho, Ha_Dec, x_Bar, S, n, CL):
        z_Statistic = (x_Bar - Ho) / (S / np.sqrt(n))
        SL = 1 - (CL / 100)

        match Ha_Dec:
            case "TWO-TAILED":
                z_Score = norm.ppf(1 - SL / 2)
                z_Stat = abs(z_Statistic)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if z_Stat >= z_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== Z-Test ===
                z_Statistic: {z_Statistic}
                Rejection Region: ±{z_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = norm.pdf(x)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=np.logical_or(x <= -z_Score, x >= z_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(-z_Score, color="black", linestyle="--", label=f"-Z Critical = {-z_Score}")
                plt.axvline(z_Score, color="black", linestyle="--", label=f"Z Critical = {z_Score}")
                plt.axvline(z_Statistic, color="green", linestyle="--", label=f"Z Statistic = {z_Statistic}")
                plt.title("Z-Test")
                plt.xlabel("Z Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

            case "LEFT":
                z_Score = norm.ppf(SL)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if z_Statistic <= z_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== Z-Test ===
                z_Statistic: {z_Statistic}
                Rejection Region: {z_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = norm.pdf(x)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=(x <= z_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(z_Score, color="black", linestyle="--", label=f"Z Critical = {z_Score}")
                plt.axvline(z_Statistic, color="green", linestyle="--", label=f"Z Statistic = {z_Statistic}")
                plt.title("Z-Test")
                plt.xlabel("Z Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

            case "RIGHT":
                z_Score = norm.ppf(1 - SL)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if z_Statistic >= z_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== Z-Test ===
                z_Statistic: {z_Statistic}
                Rejection Region: {z_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = norm.pdf(x)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=(x >= z_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(z_Score, color="black", linestyle="--", label=f"Z Critical = {z_Score}")
                plt.axvline(z_Statistic, color="green", linestyle="--", label=f"Z Statistic = {z_Statistic}")
                plt.title("Z-Test")
                plt.xlabel("Z Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

    def t_Test(self, Ho, Ha_Dec, x_Bar, S, n, CL):
        t_Statistic = (x_Bar - Ho) / (S / np.sqrt(n))
        SL = 1 - (CL / 100)
        df= n - 1

        match Ha_Dec:
            case "TWO-TAILED":
                t_Score = t.ppf(1 - SL / 2, df)
                t_Stat = abs(t_Statistic)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if t_Stat >= t_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== T-Test ===
                t_Statistic: {t_Statistic}
                Rejection Region: ±{t_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = t.pdf(x, df)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=np.logical_or(x <= -t_Score, x >= t_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(-t_Score, color="black", linestyle="--", label=f"-T Critical = {-t_Score}")
                plt.axvline(t_Score, color="black", linestyle="--", label=f"T Critical = {t_Score}")
                plt.axvline(t_Statistic, color="green", linestyle="--", label=f"T Statistic = {t_Statistic}")
                plt.title("T-Test")
                plt.xlabel("T Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

            case "LEFT":
                t_Score = t.ppf(SL, df)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if t_Statistic <= t_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== T-Test ===
                t_Statistic: {t_Statistic}
                Rejection Region: {t_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = t.pdf(x, df)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=(x <= t_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(t_Score, color="black", linestyle="--", label=f"T Critical = {t_Score}")
                plt.axvline(t_Statistic, color="green", linestyle="--", label=f"T Statistic = {t_Statistic}")
                plt.title("T-Test")
                plt.xlabel("T Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

            case "RIGHT":
                t_Score = t.ppf(1 - SL, df)

                # Decision
                decision = "disprove the null hypothesis and accept the alternative hypothesis" if t_Statistic >= t_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
                result= f"""=== T-Test ===
                t_Statistic: {t_Statistic}
                Rejection Region: {t_Score}

                Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
                there is ample evidence to {decision}."""
                print(result)

                # Plotting
                x = np.linspace(-4, 4, 1000)
                y = t.pdf(x, df)
                plt.plot(x, y, label="Standard Normal Distribution", color="blue")
                plt.fill_between(x, y, where=(x >= t_Score), color="red", alpha=0.5, label="Rejection Region")
                plt.axvline(t_Score, color="black", linestyle="--", label=f"T Critical = {t_Score}")
                plt.axvline(t_Statistic, color="green", linestyle="--", label=f"T Statistic = {t_Statistic}")
                plt.title("T-Test")
                plt.xlabel("T Score")
                plt.ylabel("Probability Density")
                plt.legend()
                plt.grid()
                plt.show()

    def ANOVA(self, SSB, dfSSB, SSW, dfSSW, CL):
        f_Statistic= (SSB / dfSSB) / (SSW / dfSSW)
        SL= 1 - (CL / 100)
        f_Score= stats.f.ppf(1 - SL, dfSSB, dfSSW)

        decision = "disprove the null hypothesis and accept the alternative hypothesis" if f_Statistic >= f_Score else "fail to reject the null hypothesis and disprove the alternative hypothesis"
        result= f"""=== One-Way ANOVA ===
        f_Statistic: {f_Statistic}
        Rejection Region: {f_Score}

        Data Analysis: Given the data of the sample as well as the Null Hypothesis mean,
        there is ample evidence to {decision}."""
        print(result)

        x = np.linspace(0, 10, 1000)
        y = stats.f.pdf(x, dfSSB, dfSSW)
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f"F-Distribution (df1={dfSSB}, df2={dfSSW})", color="blue")
        plt.fill_between(x, y, where=(x >= f_Score), color="red", alpha=0.3, label="Rejection Region")
        plt.axvline(f_Score, color="black", linestyle="--", label=f"Critical F-Value = {f_Score:.2f}")
        plt.axvline(f_Statistic, color="green", linestyle="--", label=f"F-Statistic = {f_Statistic:.2f}")
        plt.title("F-Distribution with Rejection Region")
        plt.xlabel("F-Value")
        plt.ylabel("Probability Density")
        plt.legend()
        plt.grid()
        plt.show()

    def l_Regression(self, x, y):
        slope, intercept, r_value, p_value, std_err= linregress(x, y)
        print(f"""
        Linear Regression Analysis
              Slope: {slope}
              Intercept: {intercept}
              Standard Error: {std_err}
              Linear Algebra Slope-Intercept Form: y= {slope}(x) + {intercept}""")
        
        line = [slope * xi + intercept for xi in x]
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, color="red", label="Data Points")
        plt.plot(x, line, color="black", label=f"Regression Line: y = {slope:.2f}x + {intercept:.2f}")
        plt.title("Simple Linear Regression")
        plt.xlabel("Independent Variable (x)")
        plt.ylabel("Dependent Variable (y)")
        plt.legend()
        plt.grid()
        plt.show()

    def m_Regression(self):
        y_input = input("Enter Dependent Variable values (space-separated): ")
        y = np.array(list(map(float, y_input.strip().split())))

        independent_vars = []
        while True:
            x_input = input("Enter an Independent Variable dataset (space-separated): ")
            x_values = list(map(float, x_input.strip().split()))

            if len(x_values) != len(y):
                print("Error: Independent variable length must match dependent variable length.")
                continue

            independent_vars.append(x_values)
            another = input("Do you want to add another independent variable? (Y/N): ").strip().lower()
            if another != 'y':
                break

        X = np.array(independent_vars).T
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        intercept = model.intercept_
        coefficients = model.coef_
        equation = f"Ŷ = {intercept:.4f}"

        equation = f"Ŷ = {intercept:.4f}"
        for idx, coef in enumerate(coefficients):
            equation += f" + ({coef:.4f} × X{idx+1})"
        print("Regression Equation:")
        print(equation)

        if X.shape[1] == 1:
            plt.scatter(X, y, color='blue', label='Actual')
            plt.plot(X, y_pred, color='red', label='Predicted')
            plt.xlabel("Independent Variable")
            plt.ylabel("Dependent Variable")
            plt.legend()
            plt.title("Multiple Linear Regression (1 Variable)")
            plt.show()

        elif X.shape[1] == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Actual')
            ax.scatter(X[:, 0], X[:, 1], y_pred, color='red', label='Predicted')
            ax.set_xlabel('X1')
            ax.set_ylabel('X2')
            ax.set_zlabel('Y')
            plt.title("Multiple Linear Regression (2 Variables)")
            plt.legend()
            plt.show()

    def disp_Menu(self):
        return """
        Inferential Statistics

        Hypothesis Testing
        Z-Test || T-Test || One-Way Analysis of Variance (ANOVA)
        
        Regression Analysis
        Simple Linear Regression || Multiple Linear Regression"""

inferential= infer_Stats()
while True:
    print(inferential.disp_Menu())
    inferential_Decision= input("\nEnter a Statistical Instrument: ")
    inferential_Dec= inferential_Decision.upper()

    match inferential_Dec:
        case "Z-TEST":
            while True:
                Ho= float(input("\nNull Hypothesis Value (μ₀): "))
                while True:
                    Ha= (input("Alternative Hypothesis Test (Left, Two-Tailed, Right): "))
                    Ha_Dec= Ha.upper()
                    if Ha_Dec not in ['LEFT', 'TWO-TAILED', 'RIGHT']:
                        print("Error: Enter a valid input.")
                    else:
                        break

                x_Bar= float(input("Sample Mean (𝑥̄): "))
                S= float(input("Standard Deviation (σ): "))

                while True:
                    n= float(input("Sample Size (n): "))
                    if n < 30:
                        print("Error: Sample Size below 30 utilizes a T-Test Instrument. Enter a sample size of 30 or higher.")
                    else:
                        break

                while True:
                    CL= int(input("Confidence Level (90%, 95%, 99%): "))
                    if CL not in [90, 95, 99]:
                        print("Error: Not a valid Confidence Level.")
                    else:
                        break

                print(inferential.z_Test(Ho, Ha_Dec, x_Bar, S, n, CL))
                while True:
                    z_Decision= input("\nDo you want to conduct another Z-Test? (Y/N): ")
                    z_Dec= z_Decision.upper()

                    if z_Dec == 'Y':
                        print("Repeating Z-Test...")
                        break
                    elif z_Dec == 'N':
                        break
                    else:
                        print("Error: Enter a valid input: ")

                if z_Dec == 'N':
                    break

        case "T-TEST":
            while True:
                Ho= float(input("\nNull Hypothesis Value (μ₀): "))
                while True:
                    Ha= (input("Alternative Hypothesis Test (Left, Two-Tailed, Right): "))
                    Ha_Dec= Ha.upper()
                    if Ha_Dec not in ['LEFT', 'TWO-TAILED', 'RIGHT']:
                        print("Error: Enter a valid input.")
                    else:
                        break

                x_Bar= float(input("Sample Mean (𝑥̄): "))
                S= float(input("Sample Standard Deviation (σ): "))

                while True:
                    n= float(input("Sample Size (n): "))
                    if n >= 30:
                        print("Error: Sample Size equal to or above 30 utilizes a Z-Test Instrument. Enter a sample size of 29 or below.")
                    else:
                        break

                while True:
                    CL= int(input("Confidence Level (90%, 95%, 99%): "))
                    if CL not in [90, 95, 99]:
                        print("Error: Not a valid Confidence Level.")
                    else:
                        break

                print(inferential.t_Test(Ho, Ha_Dec, x_Bar, S, n, CL))
                while True:
                    t_Decision= input("Do you want to conduct another T-Test? (Y/N): ")
                    t_Dec= t_Decision.upper()

                    if t_Dec == 'Y':
                        print("Repeating T-Test...")
                        break
                    elif t_Dec == 'N':
                        break
                    else:
                        print("Error: Enter a valid input: ")

                if t_Dec == 'N':
                    break

        case "ANOVA":
            while True:
                SSB= float(input("\nTotal Sum of Squares Between (SSB): "))
                dfSSB= float(input("Degrees of Freedom of Total Sum of Squares Between (df SSB): "))
                SSW= float(input("Total Sum of Squares Within (SSW): "))
                dfSSW= float(input("Degrees of Freedom of Total Sum of Squares Within(df SSW): "))

                while True:
                    CL= int(input("Confidence Level (90%, 95%, 99%): "))
                    if CL not in [90, 95, 99]:
                        print("Error: Not a valid Confidence Level.")
                    else:
                        break

                print(inferential.ANOVA(SSB, dfSSB, SSW, dfSSW, CL))

                while True:
                    A_Decision= input("Do you want to conduct another One-Way Anova Test? (Y/N): ")
                    A_Dec= A_Decision.upper()

                    if A_Dec == 'Y':
                        print("Repeating One-Way ANOVA test...")
                        break
                    elif A_Dec == 'N':
                        break
                    else:
                        print("Error: Enter a valid input: ")

                if A_Dec == 'N':
                    break

            
        case "SIMPLE LINEAR REGRESSION":
            while True:
                while True:
                    y_Input = input("\nDependent Variables (space-separated): ")
                    y = [float(num) for num in y_Input.split()]
                    x_Input = input("Independent Variables (space-separated): ")
                    x = [float(num) for num in x_Input.split()]

                    if len(x) != len(y):
                        print("Error: Number of Independent and Dependent values are not the same.")
                    else:
                        break

                print(inferential.l_Regression(x, y))

                while True:
                    l_Decision= input("\nDo you want to conduct another Linear Regression Analysis? (Y/N): ")
                    l_Dec= l_Decision.upper()

                    if l_Dec == 'Y':
                        print("Repeating Linear Regression Analysis Test...")
                        break
                    elif l_Dec == 'N':
                        break
                    else:
                        print("Error: Enter a valid input: ")

                if l_Dec == 'N':
                    break

        case "MULTIPLE LINEAR REGRESSION":
            print(inferential.m_Regression())

        case _:
            print("Error: Enter a valid input.")

    cont_Decision= input("Do you want to continue? (Y/N): ")
    cont_Dec= cont_Decision.upper()
    if cont_Dec == 'N':
        print("Thank you for using the program!")
        break