import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import CommentSection from "./comment";
// import { useHistory } from "react-router-dom";

function ShowReviews() {
    const [review, setReview] = useState({});
    const { id } = useParams();
 
    useEffect(() => {
        fetch( `/reviews/${id}`)
        .then(resp => resp.json())
        .then(data => setReview(data))
    }, [id])
    console.log(review)
return(
    <div>
        <h2>Users thoughts</h2>
        <p>Rating: {review.rating}</p>
        <p>Site: {review.site ? review.site.touristSite : ""}</p>
        <p>Tourist: {review.user ? review.user.username : ''}</p>

        <h3>Add Your Thoughts</h3>
        <CommentSection reviewId={review.id}/>
    </div>
)
}

export default ShowReviews;