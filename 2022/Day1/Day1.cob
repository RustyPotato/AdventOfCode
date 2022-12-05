IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
  SELECT InputFile ASSIGN TO "input1.txt"
    ORGANIZATION IS LINE SEQUENTIAL
    ACCESS IS SEQUENTIAL.

DATA DIVISION.

FILE SECTION.
FD InputFile.
01 NewerEntry PIC 99999 VALUES ZEROS.

WORKING-STORAGE SECTION.
01 FileMaximum1 PIC 999999 VALUES ZEROS.
01 FileMaximum2 PIC 999999 VALUES ZEROS.
01 FileMaximum3 PIC 999999 VALUES ZEROS.
01 GrandTotal PIC 9(6) VALUES ZEROS.
01 CurrentTotal PIC 999999 VALUES ZEROS.
01 NewestEntry PIC 99999 VALUES ZEROS.
01 EOF PIC A(1) VALUES "N".

PROCEDURE DIVISION.
    OPEN INPUT InputFile.
        PERFORM UNTIL EOF EQUALS "Y"
            READ InputFile INTO NewestEntry
                AT END MOVE 'Y' TO EOF
                NOT AT END PERFORM AddEntry
        END-PERFORM
    CLOSE InputFile.
    DISPLAY "My final answer is " FileMaximum1.
    DISPLAY "With second place being " FileMaximum2.
    DISPLAY "With third place being " FileMaximum3.
    COMPUTE Grandtotal = FileMaximum1 + FileMaximum2 + FileMaximum3.
    DISPLAY "Coming to a grand total of " GrandTotal.
    PERFORM Complete.

AddEntry.
    COMPUTE CurrentTotal = CurrentTotal + NewestEntry
    IF NewestEntry EQUAL "00000"
    THEN
        IF CurrentTotal > FileMaximum1
        THEN
            MOVE FileMaximum2 TO FileMaximum3
            MOVE FileMaximum1 TO FileMaximum2
            MOVE CurrentTotal TO FileMaximum1
        END-IF
        IF CurrentTotal < FileMaximum1 AND CurrentTotal > FileMaximum2
        THEN
          MOVE FileMaximum2 TO FileMaximum3
          MOVE CurrentTotal TO FileMaximum2
        END-IF
        IF CurrentTotal < FileMaximum2 AND CurrentTotal > FileMaximum3
        THEN
          MOVE CurrentTotal TO FileMaximum3
        END-IF
        MOVE ZEROS TO CurrentTotal
    END-IF.

Complete.
    STOP RUN.

