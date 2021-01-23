import React from 'react';
import {Button} from "../components/Button";
import renderer from 'react-test-renderer';

test('snapshot test', () => {
    const tree = renderer.create(<Button name={'Stranger'}/>).toJSON();
    expect(tree).toMatchSnapshot();
});
