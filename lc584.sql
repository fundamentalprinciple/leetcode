SELECT name
From Customer
WHERE (referee_id IS NULL) OR (referee_id!=2);
