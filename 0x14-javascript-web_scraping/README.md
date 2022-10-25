## 0x14-javascript-web_scraping

## TASKS
0. Readme
1. Write me
2. Status code
3. Star wars movie title
4. Star wars Wedge Antilles
5. Loripsum
6. How many completed?
7. Who was playing in this movie?
8. Right order





----------------------------------

##### fs.readFile
takes a callback function, which means it will not block the execution of your script. 
##### fs.readFileSync
however does not take a callback, which means that the execution of your script will be paused untill the process is finished. 

Using promisfy is one way to solve this issue, for small files it wont make a difference, but for large files you might want to transform fs.readFileSync into a promise so you wont block the execution.


----------------------------------------
fs.writeFileSync( file, data, options )

fs.writeFile( file, data, options, callback)

The Asynchronous function has a callback function as the last parameter which indicates the completion of the asynchronous function.

###### The fs.writeFileSync() is a synchronous method & creates a new file if the specified file does not exist while fs.writeFile() is an asynchronous method