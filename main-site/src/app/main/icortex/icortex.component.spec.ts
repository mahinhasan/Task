import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IcortexComponent } from './icortex.component';

describe('IcortexComponent', () => {
  let component: IcortexComponent;
  let fixture: ComponentFixture<IcortexComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [IcortexComponent]
    });
    fixture = TestBed.createComponent(IcortexComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
