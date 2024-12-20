import math as m 


import signal

# removing alram because it just crashing the program
signal.alarm = lambda x: None
text = "test.txt"

with open(text,encoding="utf-8")as f:
    contents = f.read()

#timeout funiction to replace alram
def timeout_handler():
    print("Time")


def list_to_float(list):
   for i in range(len(list)):
    list[i] = float(list[i])
   return list    



def perplexity(file):
 from pyplexity import PerplexityModel, PerplexityProcessor
 import threading
 model = PerplexityModel.from_str("bigrams-cord19")

 text_processor = PerplexityProcessor(perpl_model=model, perpl_limit=8000.0)
 
 timer = threading.Timer(5, timeout_handler)  # Timeout handler will trigger after 5 seconds
 timer.start()
 try:
    clean_text = text_processor.process(file)
 finally:
    timer.cancel()
  #formula for prepixty 
  #exp(−1/N∗sum(log(P(wi∣w 1 ,w2 ,...,w i−1 ))))
 perpl = model.compute_sentence(clean_text)
 return perpl



def sentence_length(file):
 #function to find the average length of a sentence
 # i spent longer than id like amet on this
   sentences=file.strip().split(".")
   sentences_total_words = 0

   for i in range(len(sentences)):
     
     words = sentences[i].strip().split(" ")
     words = [word for word in words if word != '']

     if words == []:
        continue
     
     sentences_total_words += len(words)
   if len(sentences) ==1:
      sentences_average = sentences_total_words
   else:
    sentences_average = sentences_total_words/(len(sentences)-1)
 
   return sentences_average




def burstiness(file):
   from re import split
   #B = (λ — k) / (λ + k):
   #B = Burstiness
   # λ = Mean inter-arrival time between bursts ##i will use arrival for this
   # k = Mean burst length
   burst_list = []
   arrival = []
   k = 1
   average_arrival = 0 
   burst = 0
   file = file.lower()
   file = file.replace('\n', ' ')
   words = split(r'[ .]+', file)
   words = [word for word in words if word]
   
   
   burst_average = 0
   
   
   for i in range(len(words)):
     arrival.clear()
     k = 1
     
  
     
     for x in range(i + 1, len(words)):
      
       if words[i] == words[x] and i!=x:
         if x-i >=0:
          k+=1
          arrival.append( x-i )
          
         else:
           print("skip")
           continue
       
      
        
    
     
       
    
     if k> 1:
        
        average_arrival = sum(arrival)/len(arrival)
        
        burst = (average_arrival-k)/(average_arrival+k)
        burst_list.append(burst)
        
        average_arrival = 0
        burst = 0
        
     

   if len(burst_list):
    burst_average = abs(sum(burst_list)/len(burst_list))
   else:
    return 0
   
   return burst_average
   

    

 
 
def readabilty(file):
   import textstat
   return textstat.flesch_reading_ease(file)
   

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    standard_deviation = m.sqrt(variance)
    return standard_deviation


with open("pep.txt") as f:
    perpl_data = f.read().split("\n")
with open("read.txt") as f:
    read_data = f.read().split("\n")
with open("burst.txt") as f:
      burst_data = f.read().split("\n")
with open("lenght.txt") as f:
      length_data = f.read().split("\n")

perpl_data=list_to_float(perpl_data)
read_data = list_to_float(read_data)
length_data = list_to_float(length_data)
burst_data = list_to_float(burst_data)

 


def is_it_ai(file):
   score =0
   train = input("is this a training run: ")
   burst = burstiness(file)
   average_sentence_lenght = sentence_length(file)
   perpl = perplexity(file)
   read = readabilty(file)
   
  

   
   if train.lower() == "yes" or train.lower() == "y":
    with open("lenght.txt","a+") as f:
           f.write("\n" +str(average_sentence_lenght))
    with open("pep.txt","a+") as f:
      f.write("\n" +str(perpl))
    with open("burst.txt","a+") as f:
      f.write("\n" +str(burst))
    with open("read.txt","a+") as f:
      f.write("\n" +str(read))
   
   
   
   
   
   

   
   mean_perpl = calculate_mean(perpl_data)
   std_peprl = calculate_standard_deviation(perpl_data)
   score += max(0, 20 - (abs(perpl - mean_perpl) / std_peprl))
   print("perplexity: ",perpl)
   print(score)
   
   mean_sentence_length = calculate_mean(length_data)
   std_length = calculate_standard_deviation(length_data)
   score += max(0, 20 - (abs(average_sentence_lenght - mean_sentence_length) / std_length))  
   print("sentence length: ",average_sentence_lenght)
   print(score)
  
   
   mean_burst = calculate_mean(burst_data)
   std_burst = calculate_standard_deviation(burst_data)
   score += max(0, 20 - (abs(burst - mean_burst) / std_burst))
   print("burstiness: ",burst)
   print(score)
   
   mean_read = calculate_mean(read_data)
   std_read = calculate_standard_deviation(read_data)
   score += max(0, 20 - (abs(read- mean_read) / std_read))
   print("readituly: ",read)
   print(score)
   
   threshold_score = 0.65 * 100 # Calculate based on empirical data
   if score <threshold_score:
    print("score: ", score)
    return "human"
   elif score >= threshold_score and score < 70:
     print(score)
     return "possilbe ai"
   elif score >= 70:
      print(score)
      return "ai"
a = is_it_ai(contents)
print(a)

