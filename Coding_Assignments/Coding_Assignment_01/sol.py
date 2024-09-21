#!/usr/bin/env python3
import matplotlib.pyplot as plt  
from typing import List
      
def numOfYears(a:int , b:int) ->int:
    """
    Implement your Logic here

    Input:
    a (int): first number
    b (int): second number

    Output:
    n (int): number of years for a to become larger than b
    """
    n = 0
    A_List = [a]
    B_List = [b]
    while a <= b:
        a *= 3
        b *= 2
        A_List.append(a)
        B_List.append(b)
        n += 1
    visualizer(A_List, B_List, n)
    return n


def visualizer(A_List:List[int], B_List:List[int], n:int) ->None:
    """
    Implement your matplot lib visualizer here
    
    Inputs:
    -------
    A (List[int]): All Height values of bar A
    B (List[int]): All Height values of bar B
    n (int): Number of years
    """
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()

    y_positions = [0, 1]
    bar_labels = ['A', 'B']

    bar_lengths = [A_List[0], B_List[0]]

    bars = ax.barh(y_positions, bar_lengths, align='center', color=['blue', 'orange'])

    ax.set_yticks(y_positions)
    ax.set_yticklabels(bar_labels)

    max_value = max(max(A_List), max(B_List)) * 1.1  
    ax.set_xlim(0, max_value)

    year_text = ax.text(0.95, 0.05, '', transform=ax.transAxes, ha='right', va='bottom')

    def init():
        for bar, length in zip(bars, [A_List[0], B_List[0]]):
            bar.set_width(length)
        year_text.set_text('Year: 0')
        return bars + (year_text,)

    def animate(i):
        for bar, length in zip(bars, [A_List[i], B_List[i]]):
            bar.set_width(length)
        year_text.set_text('Year: {}'.format(i))
        return bars + (year_text,)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n+1, interval=1000, blit=True)

    anim.save('{}_{}Bars.gif'.format(A_List[0], B_List[0]), writer='pillow')

def main() ->None:

    input_string = input("Please Enter The 2 Numbers: ")

    a, b = map(int, input_string.split())
    print("Number of years: " , numOfYears(a,b))
    plt.show()

if __name__ == "__main__":
    main()
