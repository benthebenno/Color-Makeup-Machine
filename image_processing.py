
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

#this function takes in a list of file paths as an input, and returns a list of color data
def image_processor(image_string):
  
    im = Image.open(image_string)
    px = im.load()
    color_list = []

    
    image_number_2 = Image.new('RGBA', (im.size[0], im.size[1]), (25, 25, 25, 0))
    draw = ImageDraw.Draw(image_number_2) 
    for height in range(im.size[1]):
        for width in range(im.size[0]):   
            color_tuple = px[width, height]
            largest_color = 4
            smallest_color = 4

            if color_tuple[0] > color_tuple[1] and color_tuple[0] >color_tuple[2]:
                largest_color = 0
            elif color_tuple[1] > color_tuple[0] and color_tuple[1] > color_tuple[2]:
                largest_color =1
            else:
                largest_color =2
            
            if color_tuple[0] < color_tuple[1] and color_tuple[0] <color_tuple[2]:
                smallest_color = 0
            elif color_tuple[1] < color_tuple[0] and color_tuple[1] < color_tuple[2]:
                smallest_color =1
            else:
                smallest_color =2
            
            
            percent_diffrence = ((color_tuple[largest_color] - color_tuple[smallest_color]) / (color_tuple[smallest_color]+1)) * 100
            # print(percent_diffrence)

            if color_tuple[0] >150 and color_tuple[1] >150 and color_tuple[2] <120:
                color_list.append("yellow")
                draw.point((width, height), "yellow")
            elif color_tuple[0] >150 and color_tuple[1] <120 and color_tuple[2] >150:
                color_list.append("magenta")
                draw.point((width, height),  "magenta")
            elif color_tuple[0] <120 and color_tuple[1] >150 and color_tuple[2] >150:
                color_list.append("cyan")
                draw.point((width, height),  "cyan")
            elif percent_diffrence <= 25 :
                if color_tuple[largest_color]>120 and color_tuple[largest_color]<190:
                    color_list.append("grey")
                    draw.point((width, height),  "grey")

                elif color_tuple[largest_color]>=190:
                    color_list.append("white")
                    draw.point((width, height),  "white")

                elif color_tuple[largest_color] < 120:
                    color_list.append("black")
                    draw.point((width, height),  "black")
            elif largest_color == 0:
                color_list.append("red")
                draw.point((width, height),  "red")
            elif largest_color == 1:
                color_list.append("green")
                draw.point((width, height),  "green")
            elif largest_color == 2:
                color_list.append("blue")
                draw.point((width, height), "blue")
            else:
                color_list.append("pink")
                draw.point((width, height),  "pink")
         
    image_number_2.show()
    return (color_list, im.size[0], im.size[1])
            
        
def make_graph(color_dict, is_percent, is_pie):
    colors = 'red', 'green', 'blue', 'grey', 'white', 'black', 'yellow', 'magenta','cyan' 
    colors_list = ['red', 'green', 'blue', 'grey', 'white', 'black', 'yellow', 'magenta','cyan'] 
    #print(color_dict)
    color_dict2 = color_dict
    if is_percent:
        total = color_dict['red'] + color_dict['green'] + color_dict['blue'] + color_dict['grey'] + color_dict['white'] + color_dict['black'] +color_dict['yellow'] + color_dict['magenta'] + color_dict['cyan'] 
        Runs = [(color_dict['red']/total)*100, (color_dict['green']/total)*100, (color_dict['blue']/total)*100, (color_dict['grey']/total)*100, (color_dict['white']/total)*100, (color_dict['black']/total)*100, (color_dict['yellow']/total)*100, (color_dict['magenta']/total)*100, (color_dict['cyan']/total)*100]
    else:
        Runs = [color_dict['red'], color_dict['green'], color_dict['blue'], color_dict['grey'], color_dict['white'], color_dict['black'], color_dict['yellow'], color_dict['magenta'], color_dict['cyan']]

#bar graph
    if is_pie:
        count =0
        #print(Runs)
        for percents  in Runs[:]:
            # print('what happens' + str(percents))
            if percents < 1.0:
                Runs.remove(percents)
                for entries in colors_list:
                    #print(color_dict2[entries])
                    #print(colors_list)
                    if (color_dict2[entries]/total)*100 == percents:
                        colors_list.remove(entries)

            else:
                count = count + 1
        
        explode = []    
        colors = tuple(colors_list)
       
        for i in range(count):
            explode.append(0)
        
        fig1, ax1 = plt.subplots()    
        ax1.pie(Runs, explode=explode, labels=colors, autopct='%1.1f%%',    
                shadow=True, startangle=90)    
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
        plt.show()    

    else:
        
        #print(Runs)
        plt.bar(colors,Runs,color = 'black')    
        plt.title('Result')    
        plt.xlabel('Colors')    
        plt.ylabel('Pixels of that color')    
        plt.show()    
    

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def image_processor_multiple(image_string):
  
    color_list = []
    tuple_list = []
    im = Image.open(image_string)
    px = im.load()

    for height in range(im.size[1]):
        for width in range(im.size[0]): 
            tuple_list.append(px[width, height])

 
    for color_tuple in tuple_list:

        largest_color = 4
        smallest_color = 4

        if color_tuple[0] > color_tuple[1] and color_tuple[0] >color_tuple[2]:
            largest_color = 0
        elif color_tuple[1] > color_tuple[0] and color_tuple[1] > color_tuple[2]:
            largest_color =1
        else:
            largest_color =2
        
        if color_tuple[0] < color_tuple[1] and color_tuple[0] <color_tuple[2]:
            smallest_color = 0
        elif color_tuple[1] < color_tuple[0] and color_tuple[1] < color_tuple[2]:
            smallest_color =1
        else:
            smallest_color =2
        
        
        percent_diffrence = ((color_tuple[largest_color] - color_tuple[smallest_color]) / (color_tuple[smallest_color]+1)) * 100
        # print(percent_diffrence)

        if color_tuple[0] >150 and color_tuple[1] >150 and color_tuple[2] <120:
            color_list.append("yellow")
            
        elif color_tuple[0] >150 and color_tuple[1] <120 and color_tuple[2] >150:
            color_list.append("magenta")
         
        elif color_tuple[0] <120 and color_tuple[1] >150 and color_tuple[2] >150:
            color_list.append("cyan")
       
        elif percent_diffrence <= 25 :
            if color_tuple[largest_color]>120 and color_tuple[largest_color]<190:
                color_list.append("grey")

            elif color_tuple[largest_color]>=190:
                color_list.append("white")

            elif color_tuple[largest_color] < 120:
                color_list.append("black")
            
        elif largest_color == 0:
            color_list.append("red")
        elif largest_color == 1:
            color_list.append("green")
        elif largest_color == 2:
            color_list.append("blue")
        else:
            color_list.append("pink")
         
    return (color_list)