import React, { useState, useEffect, useRef} from 'react'
import './App.css';
import Nav from './components/Nav';
import PrincipalContainer from './components/PrincipalContainer';
import Detail from './components/Detail';
import Landing from './components/Landing';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {

  const [categ, setCateg]     = useState('null')
  const [ord, setOrd]         = useState('null')
  const [ubi, setUbi]         = useState('null')

  return (
    <BrowserRouter>
      <Nav setCateg={setCateg} setOrd={setOrd} setUbi={setUbi}/>
      <Routes>
        <Route path='/' element={<Landing/>}/>
        <Route path='/todo' element={<PrincipalContainer typefilter='null' ord={ord} categ={categ} ubi={ubi}/>} />
        <Route path='/departamentos' element={<PrincipalContainer typefilter='Departamentos' ord={ord} categ={categ} ubi={ubi}/>}/>
        <Route path='/casas' element={<PrincipalContainer typefilter='Casas' ord={ord} categ={categ} ubi={ubi}/>}/>
        <Route path='/*' element={<Detail />}/>
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
