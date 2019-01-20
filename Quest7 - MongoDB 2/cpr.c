/*
Name   : Dhaval Gogri
ID     : 47444609
Course : OS - CSE7343
 */


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Clock Size or Frame Size
#define clockSize 4

// Frame number
int frameNumber[clockSize];

// Page Number that is stored in the frame
int pageStored[clockSize];

// Whether the page is in use, may be read or write
int use[clockSize];

// Whether the page is in use, may be read or write
int modify[clockSize];

//Frame Position, where the page would be replace if page not present in anty of the frame
int nextPosition = 0;

void writeClockToFile(FILE *outFilePtr, int page, char operation);




// Method for implementing and writing the result into the file.
void writeClockToFile(FILE *outFilePtr, int page, char operation){
	//	Variable used for stopping the while loop if condition is met.
	int flag = 0;
	// Write the header information into the file. i.e. page number and column
	fprintf(outFilePtr, "Page referenced: %d %c\n", page, operation);
	fprintf(outFilePtr, "      FRAME        PAGE       USE        MODIFY\n");

	while(flag != 1){
		int count = 0;
		//		First loop checks if the data is present in any frame or not.
		//		If the page is present in the frame the pointer need not go to the next frame
		// 		Use bit is set to 1 if the operation is 'r'
		//		Modify bit is set to 1 if the operation is 'w'
		for (int i = 0; i < clockSize; i++ ) {
			if(pageStored[(nextPosition + i) % clockSize] == page){
				flag = 1;
				//		Updates the bit in the respective column of the table depending on read and write.
				if(operation == 'r'){
					use[(nextPosition + i) % clockSize] = 1;
				}
				else if(operation == 'w'){
					use[(nextPosition + i) % clockSize] = 1;
					modify[(nextPosition + i) % clockSize] = 1;
				}
				break;
			}
		}

		if(flag == 0){
			//		If the page is not present int the frame, a replace has to be made.
			//			Below code does the replacement using clock page replacement algorithm
			for (int i = 0; i < clockSize; i++ ) {
				//		In the first cycle checks if the use and modify bits are set to '0'. If both are set to '0',
				//		a replacement is made.

				//		IF the condition is not true in the first cycle, while going through the second cycle,
				//		use bit is set to '0' for each pass in each frame. Also it checks if the use bit is '0' or not,
				//		during the pass and if found assigns the page to that particular frame. Modify bit can be '1'
				//		after first pass and onwards.				.
				if((use[(nextPosition + i) % clockSize] == 0 && modify[(nextPosition + i) % clockSize] == 0 && count == 0)
						|| (use[(nextPosition + i) % clockSize] == 0 && count == 1)){

					pageStored[(nextPosition + i) % clockSize] = page;
					if(operation == 'r'){
						use[(nextPosition + i) % clockSize] = 1;
						modify[(nextPosition + i) % clockSize] = 0;
					}
					else if(operation == 'w'){
						use[(nextPosition + i) % clockSize] = 1;
						modify[(nextPosition + i) % clockSize] = 1;
					}
					nextPosition = (nextPosition + i + 1) % clockSize;
					flag = 1;
					break;
				}
				if(count == 1 && flag == 0){
					use[(nextPosition + i) % clockSize] = 0;
				}
				if(i == (clockSize - 1) && flag == 0){
					count = 1;
					i = -1;
				}

			}
		}
	}
//	Below loop prints the total result in the file 'results.txt'. i.e. Prints each frame after 1 operation.
	for (int i = 0; i < clockSize; i++ ) {
		if(i == nextPosition){
			fprintf(outFilePtr, "\t%d \t    %d \t       %d \t  %d   <-- Next Frame\n", frameNumber[i], pageStored[i], use[i], modify[i]);
		}
		else{
			fprintf(outFilePtr, "\t%d \t    %d \t       %d \t  %d\n", frameNumber[i], pageStored[i], use[i], modify[i]);
		}
	}
	fprintf(outFilePtr, "\n");
}





int main(int argc, char **argv)
{
	for (int i = 0; i < clockSize; i++ ) {
		//	    Initialization of values
		frameNumber[i] = i;
		pageStored[i] = -1;
		use[i] = 0;
		modify[i] = 0;
	}

	//	Take input from file regarding page read and write
	char inFileName[ ] = "testdata.txt";
	FILE *inFilePtr = fopen(inFileName, "r");
	//	Check whether the test file is present or not for clock page replacement
	if(inFilePtr == NULL) {
		printf("File %s could not be opened.\n", inFileName);
		exit(1);
	}

	//	Creates the file if not present where the result has to be stored.
	char outFileName[ ] = "results.txt";
	FILE *outFilePtr = fopen(outFileName, "w");
	//	Checks whether file can be opened or not. Chances file cannot be opened because of file corruption.
	if(outFilePtr == NULL) {
		printf("File %s could not be opened.\n", outFileName);
		exit(1);
	}


	//	Variables where the input page number will be stored.
	int page;
	char operation;
	//	Scan the testdata.txt file and get its content
	fscanf(inFilePtr, "%d%c", &page, &operation);
	while(!feof(inFilePtr)) {
		//		Implement the clock page replacement algorithm
		writeClockToFile(outFilePtr, page, operation);
		//		Used for moving to the next character
		fscanf(inFilePtr, "%d%c", &page, &operation);
	}

	// closing the file as it is not needed further.
	fclose(inFilePtr);
	fclose(outFilePtr);
	exit(0);
}
