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
01 GrandTotal PIC 9(6) VALUES ZEROS.
01 MatchScore PIC 9(1) VALUES ZEROS.
01 NewestEntry.
  02 TheirMove PIC X(1) VALUES ZEROS.
  02 Empty PIC X(1) VALUES SPACE.
  02 MyMove PIC X(1) VALUES SPACE.
01 EOF PIC A(1) VALUES "N".

PROCEDURE DIVISION.
    OPEN INPUT InputFile.
        PERFORM UNTIL EOF EQUALS "Y"
            READ InputFile INTO NewestEntry
                AT END MOVE 'Y' TO EOF
                NOT AT END PERFORM AddEntry
        END-PERFORM
    CLOSE InputFile.
    DISPLAY "Coming to a grand total of " GrandTotal.
    PERFORM Complete.

AddEntry.
    MOVE ZEROS TO MatchScore
    IF (MyMove = "X")
        COMPUTE MatchScore = MatchScore + 1
    END-IF.
    IF (MyMove = "Y")
        COMPUTE MatchScore = MatchScore + 2
    END-IF.
    IF (MyMove = "Z")
        COMPUTE MatchScore = MatchScore + 3
    END-IF.

    IF (TheirMove = "A" AND MyMove = "X") OR
       (TheirMove = "B" AND MyMove = "Y") OR
       (TheirMove = "C" AND MyMove = "Z")
        COMPUTE MatchScore = MatchScore + 3
    END-IF.
    IF (TheirMove = "A" AND MyMove = "Y") OR
       (TheirMove = "B" AND MyMove = "Z") OR
       (TheirMove = "C" AND MyMove = "X")
    THEN
        COMPUTE MatchScore = MatchScore + 6
    END-IF.

    COMPUTE GrandTotal = GrandTotal + MatchScore.

Complete.
    STOP RUN.

