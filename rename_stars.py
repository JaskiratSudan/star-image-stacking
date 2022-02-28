import os



def rename_song():
  
   i = 0
   path="images/"
   for filename in os.listdir(path):
      my_dest ="star" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1







if __name__ == "__main__":

    rename_song()
