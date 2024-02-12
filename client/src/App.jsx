import {Route, Routes} from "react-router-dom";
import Header from './Header'
import Home from "./Home";
import ShowReviews from "./Review"
import Site from "./site";
import './App.css'
import CommentSection from "./comment";

function App() {

  return (
    <>
      <div>
        <Header />
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/:id" element={<Site/>}/>
          <Route exact path="/:id/showreview/:id" element={<ShowReviews/>}/>
          <Route exact path="/:id/showreview/:id" element={<CommentSection />}/>
        </Routes>
       
      </div>
    </>
  )
}

export default App
