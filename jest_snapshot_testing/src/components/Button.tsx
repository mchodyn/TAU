import React from 'react';
import './Button.css'

interface buttonProps {
    name:string;
}

export const Button:React.FC<buttonProps> = props => {
    return (<button onClick={()=> window.alert(`Hello ${props.name}`)}>Changed text!</button>)
}

