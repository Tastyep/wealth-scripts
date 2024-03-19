#!/bin/python

import argparse

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(
                    prog='Invest',
                    description='Simulate invest payoff over time',
                    epilog='')
    
    # Adding Arguments
    parser.add_argument('amount', type=float, help='Principal invest amount')
    parser.add_argument('-y', '--years', type=int, default=30, help='Number of years')
    parser.add_argument('-r', '--rate', type=float, default=5.0, help='Interest rate in percent')
    parser.add_argument('-i', '--income', type=float, default=1500.0, help='Monthly investment')
    
    # Parse Arguments
    args = parser.parse_args()
    
    amount = args.amount
    rate = args.rate / 100
    invested = amount
    for _ in range(args.years):
        interest = amount * rate
        yearly_investment = (args.income * 12)
        invested += yearly_investment
        amount += interest + yearly_investment

    total_interest = amount - invested
    monthly_earnings = (amount * rate) / 12
    print(f"Total: {amount:,.2f} | Invested: {invested:,.2f} | Interest: {total_interest:,.2f} | Monthly: {monthly_earnings:,.2f}")

if __name__ == "__main__":
    main()


