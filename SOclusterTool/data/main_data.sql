USE stackoverflow;

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Tags/Tags.xml'
INTO TABLE Posts
ROWS identified BY '<row>';

DELETE FROM Badges;

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Badges/Badges.xml'
INTO TABLE Badges
ROWS identified BY '<row>';

DELETE FROM Comments;

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Comments/Comments.xml'
INTO TABLE Comments
ROWS identified BY '<row>';

DELETE FROM Posts;

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Tags/Tags.xml'
INTO TABLE Tags
ROWS identified BY '<row>';