---
categories:
- bad
date: 2014-11-05 11:12:45+10:00
next:
  text: '"Established versus Affordances: part of the reason institutional e-learning
    is like teenage sex"'
  url: /blog2/2014/11/07/established-versus-affordances-part-of-the-reason-institutional-e-learning-is-like-teenage-sex/
previous:
  text: Fixing one part of the peoplesoft gradebook
  url: /blog2/2014/10/14/fixing-one-part-of-the-peoplesoft-gradebook/
title: Some more tweaks to gradebook
type: post
template: blog-post.html
---
This is a development log of a few additions to the [recent fixes to the Peoplesoft gradebook](/blog2/2014/10/14/fixing-one-part-of-the-peoplesoft-gradebook/). The following documents attempts to implement the following

1. **Highlight students in the supp range** DONE Students with a mark between 44.5 and 49.5 need the grade to be set to IM and a note inserted.
2. **PE overrides** DONE Courses with a professional experience component need to have the default FNC over-ridden when they don't have a PE mark yet. And a comment also needs inserting.

The second is harder because the page being updated doesn't contain the PE mark. A bit more challenging to implement.

And thanks to a "communique" there's a more complete set of "guidelines on the allocation of marks and final grades" which lists

1. Round up when total marks a close to grade cut-offs - DONE.
2. Review where the total marks a close to the passing grade cut-off.
    
    This is the "supp" range task.
    
3. Review where the total marks are close to higher grade cut-offs.
    
    This appears to be a duplication of #1, but includes the phrase "review the performance". I wonder why if the mark has already been rounded up?
    
4. Allocation of supplementary grades. - DONE
    
    Any student within 5% below the passing mark and who has complete all assessment can be given a supplementary IS/IM. Similar to the "PE Overrides" above in terms of how it would have to work.
    

# Left to do

1. **Handle the process of saving** Once you save the gradebook, it won't run the update again to show the changes. More kludging to do I feel. Appears to be due to the fact that the "saving" process takes a long time and this defeats the "pause before running" kludge currently used to update the rows.
2. **Give advice on the different types of fails.** If a student has submitted all assessment items but failed the course, they should get an F. If they submitted some, but not all assessment items, then the grade should be a FNC. If they didn't submit any assessment items, the grade should be a FNP.
    
    The process used to check for PE could be expanded to handle this.
3. **Checking on institutional MOE** Can they install Firefox/Greasemonkey?
4. **Checking on the process used by others** The sequence of steps I use in the gradebook may not match what others use. Observe what they do.

# Supp range

Basic task is to

1. Recognise students in the grade range. Easy. \[code lang="javascript"\] } else if ( isSuppRange( rawResult )) { changeBackground( element, studentNum, "#FFCC00" ); } \[/code\]
    
2. Change the background color. Let's go #FFCC00.
3. Add in some reminder about adding a note? The div win0divSTDNT\_GRADE\_HDR\_EMPLID$3 (where 3 is the student number) seems like a good place to add the warning/explanation.
    
    Have identified the element in the script. Need to figure out how to add some text into it. Showing up as XrayWrapper object HTMLDivElement. Ahh, just how simple it is when you aren't ignorant. \[code lang="javascript"\] element.getElementById( id ).insertAdjacentHTML('beforeend', newHTML ); \[/code\]
4. Check all the options
    - Award a supplementary grade DONE
    - Upgrade on the border line - no change DONE
    - Upgrade on the border line - change made DONE

# PE overrides

The requirement here is to

1. Detect any student that doesn't have a result for "practicum".
2. Advise that the mark needs to change to a "result outstanding".

This is complicated because the page on which staff can change the result, does not contain any information about the practicum result. It does appear on the first gradebook page displayed, but not the change page. So the script will need to

1. Save the practicum result for all the students on the first page. It appears that the [GM\_setValue](http://wiki.greasespot.net/GM_setValue) function is a way to do this. When the first page is loaded, the values will need to be extracted and stored. So sub-steps
    - Detect that the first page has been loaded. So how to identify the first page?
        
        Actually, not really interested in if it is the first page. Just look for if it has the word PRACTICUM in the header of a specific table.
        
        \[code lang="javascript"\] var description = 1; var id = "DERIVED\_LAM\_ASSIGNMENT\_DESCR\_" + description + "$0"; var name = frame.getElementById( id );
        
        // loop through all the assignment descriptions for first row while ( name ) { var rawResult = name\["textContent"\];
        
        if ( rawResult == "PRACTICUM" ) { return true; } \[/code\]
        
    - Extract the practicum values Will need to extract the column number for the practicum results ...it will be located in an input box with the id DERIVED\_LAM\_GRADE\_1$0 where 1 is the column (first column with results - and matching the column in which practicum was found) and 0 is the student number in the row.
        
        Will need to extract the matching ID number so that the practicum result is saved for that student. The student's ID number is located in a span with the id STDNT\_GRADE\_HDR\_EMPLID$0
        
        \[code lang="javascript"\] var studentNum = 0; var peResultID = "DERIVED\_LAM\_GRADE\_" + column + "$" + studentNum; var peResultElement = frame.getElementById( peResultID ); var studentID = "STDNT\_GRADE\_HDR\_EMPLID$" + studentNum; var studentElement = frame.getElementById( studentID );
        
        // loop through all the rows in the table while ( peResultElement ) { var rawResult = peResultElement.value; var studentRaw = studentElement\["textContent"\];
        
        var id = "STUDENT\_peResult\_" + studentRaw; GM\_setValue( id, rawResult ); \[/code\]
        
    - Save them. The question now is how and what to save. Perhaps the aim here is only to save those students who do NOT have a result? Or should we save them all? i.e. actually save a value for all STUDENT\_peResult\__id_ The code above has the modified version.
2. Use that stored information on the change page. When we're checking the other page, need to add in a getValue call to test it.
3. Should think about deleting the values when the script is on the first page. Just to make sure there aren't any left overs? But then if you have to go to this page first, then it should be ok as it gets overwriten. \[code lang="javascript"\] var keys = GM\_listValues(); for ( var i=0; i < keys.length; i++ ) { var t = GM\_getValue( keys\[i\] ); if ( keys\[i\].match( /^STUDENT\_peResult\_/ ) ) { GM\_deleteValue( keys\[i\] ); } } \[/code\]
4. PE results missing for all. PE results don't get entered until late in the process. So if you visit the gradebook before this you get the PE result over-riding everything else. Need to prevent this from happening. i.e. if there are no PE results for anyone, then don't display this warning. Done.