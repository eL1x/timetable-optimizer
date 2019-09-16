import matplotlib.pyplot as plt
from src.configuration import *

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
colors = ['pink', 'lightgreen', 'lightblue', 'wheat', 'salmon']
day_label = 'Timetable'

fig_width = 10
fig_height = 6


def convert_hour(hour):
    return STARTING_HOUR + hour * DIFFERENCE_BETWEEN_STARTING_CLASSES_IN_HOURS


def convert_hour_to_text(hour):
    return (STARTING_HOUR + hour * DIFFERENCE_BETWEEN_STARTING_CLASSES // MINUTES_IN_HOUR,
            hour * DIFFERENCE_BETWEEN_STARTING_CLASSES % MINUTES_IN_HOUR)


def plot_timetable(student):
    fig = plt.figure(figsize=(fig_width, fig_height))

    for classwork in student.timetable:
        classwork_name = classwork.classwork_name

        day = classwork.day + 0.52
        start_hour = convert_hour(classwork.hour)
        end_hour = start_hour + DURATION_OF_ONE_CLASSWORK_IN_HOURS

        plt.fill_between([day, day + 0.96], [start_hour, start_hour], [end_hour, end_hour],
                         color=colors[int(day)], edgecolor='k', linewidth=0.5)

        timetable_hour = convert_hour_to_text(classwork.hour)
        plt.text(day + 0.02, start_hour + 0.05, '{0}:{1:0>2}'.format(int(timetable_hour[0]), int(timetable_hour[1])),
                 va='top', fontsize=7)

        plt.text(day + 0.48, (start_hour + end_hour) * 0.5, classwork_name, ha='center', va='center', fontsize=11)

    ax = fig.add_subplot(111)
    ax.yaxis.grid()
    ax.set_xlim(0.5, len(days) + 0.5)
    ax.set_ylim(20, 8)
    ax.set_xticks(range(1, len(days) + 1))
    ax.set_xticklabels(days)
    ax.set_ylabel('Time')

    ax2 = ax.twiny().twinx()
    ax2.set_xlim(ax.get_xlim())
    ax2.set_ylim(ax.get_ylim())
    ax2.set_xticks(ax.get_xticks())
    ax2.set_xticklabels(days)
    ax2.set_ylabel('Time')

    plt.title(day_label, y=1.07)

    plt.show()

