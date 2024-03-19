#!/bin/python

import argparse

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(
                    prog='Debt',
                    description='Simulate debt payoff over time',
                    epilog='')
    
    # Adding Arguments
    parser.add_argument('amount', type=float, help='Principal loan amount')
    parser.add_argument('-y', '--years', type=int, default=30, help='Number of years')
    parser.add_argument('-r', '--rate', type=float, default=5.0, help='Interest rate in percent')
    
    # Parse Arguments
    args = parser.parse_args()
    
    amount = args.amount
    months = args.years * 12
    rate  =args.rate / 100
    monthly_rate = rate / 12
    ci = pow(1 + monthly_rate, months)
    monthly_cost = amount * ((monthly_rate * ci) / (ci - 1))
    total_payment = monthly_cost * months
    total_interest = total_payment - amount

    print(f"Total: {total_payment:,.2f} | Interest: {total_interest:,.2f} | Monthly: {monthly_cost:,.2f}")

if __name__ == "__main__":
    main()


