from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False)->str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...
    
    if labels != None:
        # Converting the items of rows=[[]] and labels[] into string
        rows = [list(map(str, i)) for i in rows]
        labels = list(map(str, labels))

        # Finding the maxwidth for each of the column and storing them in a list
        max_column_width = []
        for columns in zip(labels,*rows):
            columns = list(columns)
            max_column_width.append(len(max(columns, key=len)))


        # Creates new table with label = table[0] and rows = table[1]
        table = [labels, rows]

        # Widthlen is the maximum length for calculating the quantity of '---' such borders
        widthlen = int()
        start = -1
        for i in labels:
            widthlen += len(i)+ (abs(max_column_width[labels.index(i, start + 1)]-len(i)))
            start +=1

        # General formula for calculating the extra space length relative to the column length
        # (2n -1)+n 
        label_len = ((2*len(labels))-1)+len(labels)

    # Above label decoration
        header = "┌"+(chr(9472)*(widthlen+label_len))+"┐"

        headerlst=[]
        for i in header:
            headerlst += i

    # Appending the indexes to properly substitute headerlist with replacements
        indexes = []
        for i in max_column_width:
            # 3 is for the extra space excluding the relative column space and item
            indexes.append(i+3)
        for i in range(len(indexes)):
            if i>0:
                indexes[i] = indexes[i]+indexes[i-1]


        replacements = ['┬']*(len(table[0])-1)
        for(index, replacement) in zip(indexes, replacements):
            headerlst[index] = replacement
        
        upper_label_border = f'{"".join(headerlst)}\n'

        # NOTE: I USED 'START' THROUGHTOUT TO HANDLE THE DUPLICATE ITEMS POINTING TO THE SAME INDEX
        print1 = []
        start = -1
        print1start=0
        if centered==True:
            for data in labels:
                if (abs(max_column_width[labels.index(data, start+1)]-len(data))) % 2 != 0:
                    print1.append(f'│ {chr(32)*(abs(max_column_width[labels.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[labels.index(data, start+1)]-len(data))//2)}  ')
                else:
                    print1.append(f'│ {chr(32)*(abs(max_column_width[labels.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[labels.index(data, start+1)]-len(data))//2)} ')
                if table[0].index(data, start+1)==(len(table[0])-1):
                    print1[print1start] += '│\n'
                print1start+=1
                start += 1
        else:

            for i in labels:
                print1.append(f'│ {i}{chr(32)*abs(max_column_width[labels.index(i, start+1)]-len(i))} ')
                if labels.index(i, start+1)==(len(labels)-1):
                    print1[print1start] += '│\n'
                print1start+=1
                start += 1

    # Below label decoration
        header = '├'+(chr(9472)*(widthlen+label_len))+'┤'
        headerlst1=[]
        for i in header:
            headerlst1 += i
        replacements = ['┼']*(len(table[0])-1)
        for(index, replacement) in zip(indexes, replacements):
            headerlst1[index] = replacement
        
        below_label_border = f'{"".join(headerlst1)}\n'


    # Printing rows
        print2 = []
        start = -1
        print1start=0
        if centered==True:
            for row in table[1]:
                for data in row:
                    if (abs(max_column_width[row.index(data, start+1)]-len(data))) % 2 != 0:
                        print2.append(f'│ {chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}  ')
                    else:
                        print2.append(f'│ {chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)} ')
                    if row.index(data, start+1)==(len(row)-1):
                        print2[print1start] += '│\n'
                    print1start+=1 
                    start += 1
                start = -1
        else:
            start = -1
            for row in table[1]:
                for item in row:
                    print2.append(f'│ {item}{chr(32)*abs(max_column_width[row.index(item, start+1)]-len(item))} ')
                    if row.index(item, start+1)==(len(row)-1):
                        print2[print1start-1] += '│\n'
                    start += 1
                start = -1

    # Print the footer
        header = "└"+(chr(9472)*(widthlen+label_len))+"┘"
        headerlst3=[]
        for i in header:
            headerlst3 += i
        replacements = ['┴']*(len(table[0])-1)
        for(index, replacement) in zip(indexes, replacements):
            headerlst3[index] = replacement
        
        below_row_border = f'{"".join(headerlst3)}\n'

        return upper_label_border+''.join(print1)+below_label_border+''.join(print2)+below_row_border

# IF ONLY ROWS ----------------->>>>>>>>>
    else: 
        rows = [list(map(str, i)) for i in rows]

    # Storing the maximum max_column_width in each column
        max_column_width = []
        for columns in zip(*rows):
            columns = list(columns)
            max_column_width.append(len(max(columns, key=len)))


    # General formula for calculating the extra space length
    # (2n -1)+n 
    # Relative to the no of items, so the exact row doesn't matter
        extra_space_length = ((2*len(rows[0]))-1)+len(rows[0])


    # For printing '-----':  item + extraspace
        max_column_widthlen = int()
        start = -1
        for i in rows[0]:
            max_column_widthlen += len(i)+ (abs(max_column_width[rows[0].index(i, start+1)]-len(i)))
            start += 1

    # Finding the indexes for replacing them with ┬ and such
        indexes = []
        for i in max_column_width:
            indexes.append(i+3)
        for i in range(len(indexes)):
            if i>0:
                indexes[i] = indexes[i]+indexes[i-1]


        header = "┌"+(chr(9472)*(max_column_widthlen+extra_space_length))+"┐"
        headerlst=[]
        for i in header:
            headerlst += i
    
        replacements = ['┬']*(len(rows[0])-1)
        for(index, replacement) in zip(indexes, replacements):
            headerlst[index] = replacement
        
        above_row_border = f'{"".join(headerlst)}\n'

    # Print rows
        print1=[]
        start=-1
        print1start = 0
        if centered==True:
            start = -1
            for row in rows:
                for data in row:
                    # printing fashion: | item{spaces} |
                    if (abs(max_column_width[row.index(data, start+1)]-len(data))) % 2 != 0:
                        print1.append(f'│ {chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}  ')
                    else:
                        print1.append(f'│ {chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)}{data}{chr(32)*(abs(max_column_width[row.index(data, start+1)]-len(data))//2)} ')
                    if row.index(data, start+1)==(len(row)-1):
                        print1[print1start] += '│\n'
                    print1start += 1
                    start += 1
                start = -1   
        else:  
            for row in rows:
                for data in row:
            # print: | item{spaces} |
                    print1.append(f'│ {data}{" "*abs(max_column_width[row.index(data, start+1)]-len(data))} ')
                    if row.index(data, start+1)==(len(row)-1):
                        print1[print1start] += '│\n'
                    print1start += 1
                    start += 1
                start=-1

        #print footer
        header = "└"+(chr(9472)*(max_column_widthlen+extra_space_length))+"┘"

        headerlst=[]
        for i in header:
            headerlst += i

        replacements = ['┴']*(len(rows[0])-1)
        for(index, replacement) in zip(indexes, replacements):
            headerlst[index] = replacement
        
        below_row_border = f'{"".join(headerlst)}\n'

        return above_row_border+''.join(print1)+below_row_border
