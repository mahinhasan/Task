import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcedemicComponent } from './acedemic.component';

describe('AcedemicComponent', () => {
  let component: AcedemicComponent;
  let fixture: ComponentFixture<AcedemicComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AcedemicComponent]
    });
    fixture = TestBed.createComponent(AcedemicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
