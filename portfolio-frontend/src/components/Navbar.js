import React from 'react'
import { Link } from 'react-router-dom'
function Navbar() {
  return (
    <div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href="/">Navbar</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div className="navbar-nav">
                        <Link className="nav-link active" aria-current="page" to="/">Home</Link>
                        <Link className="nav-link" to="/blogs">Blog</Link>
                        <Link className="nav-link" to="/project">Projects</Link>
                    </div>
                </div>
            </div>
            <div class="form-check form-switch d-flex">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked"/>
                <label class="form-check-label" htmlFor="flexSwitchCheckChecked">DarkMode</label>
            </div>
        </nav>
    </div>
  )
}

export default Navbar
