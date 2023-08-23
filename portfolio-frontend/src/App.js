import './App.css';
import AboutMe from './components/AboutMe';
import Blogs from './components/Blogs';
import Navbar from './components/Navbar';
import Experience from './components/Experience';
import Projects from './components/Projects';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <>
    <Router>
        
        <Navbar/>
        <Routes>
            <Route exact path="/" element={<AboutMe/>}/>
            <Route exact path="/blogs" element={<Blogs/>}/>
            <Route exact path="/experience" element={<Experience/>}/>
            <Route exact path="/project" element={<Projects/>}/>
        </Routes>
    </Router>
    
    </>
  );
}

export default App;
