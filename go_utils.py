from AlphaGo import go
import io
def plot_board(board,figsize=(5,5),
                        should_plot=True, western_column_notation=True,next_step=None):
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
    except ImportError as e:
        print(
            'Failed to import matplotlib. This is an optional dependency of ' +
            'the RocAlphaGo project, so it is not included in the requirements file. ' +
            'You must install matplotlib yourself to use the plotting functions.')
        raise e

    from distutils.version import StrictVersion
    matplotlib_version = matplotlib.__version__
    if StrictVersion(matplotlib_version) < StrictVersion('1.5.1'):
        print('Your version of matplotlib might not support our use of it')

    # Initial matplotlib setup
    fig, ax = plt.subplots(figsize=figsize)
    plt.xlim([0, board.shape[0] + 1])
    plt.ylim([0, board.shape[1] + 1])

    # Wooden background color
    ax.set_axis_bgcolor('#fec97b')
    plt.gca().invert_yaxis()

    # Setup ticks
    ax.tick_params(axis='both', length=0, width=0)
    # Western notation has the origin at the lower-left
    if western_column_notation:
        plt.xticks(range(1, board.shape[0] + 1), range(1, board.shape[0] + 1))
        plt.yticks(range(1, board.shape[0] + 1), reversed(range(1, board.shape[0] + 1)))
    # Traditional has the origin at the upper-left and uses letters minus 'I' along the top
    else:
        ax.xaxis.tick_top()
        plt.xticks(range(1, board.shape[0] + 1), [x for x in LETTERS[:board.shape[0] + 1] if x != 'I'])
        plt.yticks(range(1, board.shape[0] + 1), range(1, board.shape[0] + 1))

    # Draw grid
    for i in range(board.shape[0]):
        plt.plot([1, board.shape[0]], [i + 1, i + 1], lw=1, color='k', zorder=0)
    for i in range(board.shape[0]):
        plt.plot([i + 1, i + 1], [1, board.shape[0]], lw=1, color='k', zorder=0)

 
    # Display stones already played
    stone_x_coords = []
    stone_y_coords = []
    stone_colors = []
    for i in range(board.shape[0]):
        for j in range(board.shape[0]):
            if board[i][j] != go.EMPTY:
                stone_x_coords.append(i + 1)
                stone_y_coords.append(j + 1)
                if board[i][j] == go.BLACK:
                    stone_colors.append('black')
                else:
                    stone_colors.append('white')
    
    plt.scatter(stone_x_coords, stone_y_coords, marker='o', edgecolors='k',
                s=150, c=stone_colors, zorder=4)
    if next_step:
        plt.scatter([next_step[0] + 1], [next_step[1] + 1], marker='o', edgecolors='k',
                s=150, c='black', zorder=4)
        plt.scatter([next_step[0] + 1], [next_step[1] + 1], marker='o', edgecolors='k',
                s=15, c='red', zorder=4)

    
    if should_plot:
        plt.show()
    plt.close()
    
def draw_board(board,figsize=(5,5),
                        should_plot=True, western_column_notation=True,next_step=None):
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
    except ImportError as e:
        print(
            'Failed to import matplotlib. This is an optional dependency of ' +
            'the RocAlphaGo project, so it is not included in the requirements file. ' +
            'You must install matplotlib yourself to use the plotting functions.')
        raise e

    from distutils.version import StrictVersion
    matplotlib_version = matplotlib.__version__
    if StrictVersion(matplotlib_version) < StrictVersion('1.5.1'):
        print('Your version of matplotlib might not support our use of it')

    # Initial matplotlib setup
    fig, ax = plt.subplots(figsize=figsize)
    plt.xlim([0, board.shape[0] + 1])
    plt.ylim([0, board.shape[1] + 1])

    # Wooden background color
    ax.set_axis_bgcolor('#fec97b')
    plt.gca().invert_yaxis()

    # Setup ticks
    ax.tick_params(axis='both', length=0, width=0)
    # Western notation has the origin at the lower-left
    if western_column_notation:
        plt.xticks(range(1, board.shape[0] + 1), range(1, board.shape[0] + 1))
        plt.yticks(range(1, board.shape[0] + 1), reversed(range(1, board.shape[0] + 1)))
    # Traditional has the origin at the upper-left and uses letters minus 'I' along the top
    else:
        ax.xaxis.tick_top()
        plt.xticks(range(1, board.shape[0] + 1), [x for x in LETTERS[:board.shape[0] + 1] if x != 'I'])
        plt.yticks(range(1, board.shape[0] + 1), range(1, board.shape[0] + 1))

    # Draw grid
    for i in range(board.shape[0]):
        plt.plot([1, board.shape[0]], [i + 1, i + 1], lw=1, color='k', zorder=0)
    for i in range(board.shape[0]):
        plt.plot([i + 1, i + 1], [1, board.shape[0]], lw=1, color='k', zorder=0)

 
    # Display stones already played
    stone_x_coords = []
    stone_y_coords = []
    stone_colors = []
    for i in range(board.shape[0]):
        for j in range(board.shape[0]):
            if board[i][j] != go.EMPTY:
                stone_x_coords.append(i + 1)
                stone_y_coords.append(j + 1)
                if board[i][j] == go.BLACK:
                    stone_colors.append('black')
                else:
                    stone_colors.append('white')
    
    plt.scatter(stone_x_coords, stone_y_coords, marker='o', edgecolors='k',
                s=150, c=stone_colors, zorder=4)
    if next_step:
        plt.scatter([next_step[0] + 1], [next_step[1] + 1], marker='o', edgecolors='k',
                s=150, c='black', zorder=4)
        plt.scatter([next_step[0] + 1], [next_step[1] + 1], marker='o', edgecolors='k',
                s=15, c='red', zorder=4)

    
    #if should_plot:
    #    plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    #plt.savefig('test.png')
    buf.seek(0)
    plt.close()
    return buf
    