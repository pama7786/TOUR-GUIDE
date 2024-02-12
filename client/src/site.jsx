import { useEffect, useState } from "react";
import {  Link, useParams } from "react-router-dom"

function Site(){
        const [ sites, setSites] = useState({})
        const { id } = useParams();
        const [visitorCount, setVisitorCount] = useState(0);

        useEffect(() => {
            fetch(`/sites/${id}`)
            .then(resp => resp.json())
            .then(data => {
                setSites(data);
            })
        }, [id]);

        const countNoOfVisitors = () => {
            setVisitorCount((lastCount) => lastCount + 1);
        }

        return(
            <div>
                <h2>Site Details</h2>
                
                    {/* {sites.map((review) => (
                        <p key={sites.id}>
                        </p> */}
                        <p>Location: {sites.location}</p>
                        <p>Description: <Link to={`showreview/${sites.id}`}>{sites.description}</Link></p> 

                    <p>Rating: {sites.rating}</p>
                <div id="click"><button onClick={countNoOfVisitors}>
                    Tap if you like the info
                </button>
                <p>Like Count: {visitorCount}</p>

                </div>
                
            </div>
        )
}

export default Site;
