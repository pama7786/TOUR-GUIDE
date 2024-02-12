import  { useState  } from "react";

function CommentSection(){
    const [newcomments, setNewComments] = useState("");

    const handleCommentSubmit = ({newId}) => {
        setNewComments("");
        fetch("/reviews", {
          method: "POST",
          headers:{
            'Content-Type':"application/json"
          },
          body:JSON.stringify(newId)
        })
        .then(resp => resp.json())
    };
    return (
        <div id="comment">
        <textarea
          rows="3"
          cols="30"
          value={newcomments}
          onChange={(e) => setNewComments(e.target.value)}
        />
        <button onClick={handleCommentSubmit}>Submit Comment</button>
      </div>
    );
}

export default CommentSection;